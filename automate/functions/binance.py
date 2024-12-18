from binance.spot import Spot
from binance.cm_futures import CMFutures
from binance.um_futures import UMFutures
from binance.error import ClientError

def check_binance_credentials(api_key, api_secret, trade_type="S"):
    try:
        if trade_type == "S":  # Spot
            client = Spot(api_key, api_secret)
            client.account()
        elif trade_type == "U":  # USDM
            client = UMFutures(api_key, api_secret)
            client.account()
        elif trade_type == "C":  # COINM
            client = CMFutures(api_key, api_secret)
            client.account()
        else:
            return {'error': "Invalid trade type specified. Choose 'spot', 'usdm', or 'coinm'.", "valid": False}

        return {'message': "API credentials are valid.", "valid": True}
    
    except ClientError as e:
        return {"error": e.error_message}
    except Exception as e:
        return {"error": str(e)}

def get_account_balance(binance_account, asset: str):
    try:
        trade_type = binance_account.type
        balances = {}

        if trade_type == "S":  # Spot
            client = Spot(api_key=binance_account.apiKey, api_secret=binance_account.secretKey)
            account_info = client.account()
            for balance in account_info['balances']:
                balances[balance['asset']] = float(balance['free'])
        elif trade_type in ["U", "C"]:  # USDM or COINM Futures
            if trade_type == "U":
                client = UMFutures(key=binance_account.apiKey, secret=binance_account.secretKey)
            else:
                client = CMFutures(key=binance_account.apiKey, secret=binance_account.secretKey)
            account_info = client.account()
            for balance in account_info['assets']:
                balances[balance['asset']] = float(balance['availableBalance'])
        else:
            raise ValueError("Invalid trade type. Use 'spot', 'usdm', or 'coinm'.")

        return {"asset": asset, "balance": balances.get(asset, 0.0)}
    
    except ClientError as e:
        raise ValueError(e.error_message)
    except Exception as e:
        raise ValueError(str(e))

def adjust_trade_quantity(binance_account, symbol, quote_order_qty):
    try:
        # Fetch balance based on the trade type
        if binance_account.trade_type == "S":  # Spot
            base_asset, quote_asset = symbol.split("/")
            base_balance = get_account_balance(binance_account, base_asset)["balance"]
            quote_balance = get_account_balance(binance_account, quote_asset)["balance"]

            if base_balance < quote_order_qty:
                return base_balance
            elif quote_balance < quote_order_qty:
                raise ValueError("Insufficient funds in the quote asset balance.")

            return quote_order_qty
        elif binance_account.trade_type in ["U", "C"]:  # USDM or COINM Futures
            # Futures balances are assumed to be in the margin account
            margin_balance = get_account_balance(binance_account, "USDT")["balance"]
            if margin_balance < quote_order_qty:
                return margin_balance
            return quote_order_qty
        else:
            raise ValueError("Invalid trade type. Use 'spot', 'usdm', or 'coinm'.")
    
    except Exception as e:
        raise ValueError(str(e))

def open_binance_trade(binance_account, symbol: str, side: str, quantity: float, custom_id: str = None):
    try:
        adjusted_quantity = adjust_trade_quantity(binance_account, symbol, float(quantity))
        trade_type = binance_account.type

        order_params = {
            "symbol": symbol,
            "side": str.upper(side),
            "type": "MARKET",
            "quantity": adjusted_quantity,
        }

        if trade_type == "S":
            client = Spot(api_key=binance_account.apiKey, api_secret=binance_account.secretKey)
            response = client.new_order(**order_params)
        elif trade_type == "U":
            client = UMFutures(key=binance_account.apiKey, secret=binance_account.secretKey)
            response = client.new_order(**order_params)
        elif trade_type == "C":
            client = CMFutures(key=binance_account.apiKey, secret=binance_account.secretKey)
            response = client.new_order(**order_params)
        else:
            raise ValueError("Invalid trade type. Use 'spot', 'usdm', or 'coinm'.")

        return {
            "order_id": response["orderId"],
            "symbol": response["symbol"],
            "side": response["side"],
            "price": response.get("fills", [{}])[0].get("price", "0"),
            "quantity": response["origQty"],
        }
    
    except ClientError as e:
        raise ValueError(e.error_message)
    except Exception as e:
        raise ValueError(str(e))

def close_binance_trade(binance_account, symbol: str, side: str, quantity: float):
    try:
        adjusted_quantity = adjust_trade_quantity(binance_account, symbol, float(quantity))
        t_side = "SELL" if side.upper() == "BUY" else "BUY"
        order_params = {
            "symbol": symbol,
            "side": str.upper(t_side),
            "type": "MARKET",
            "quantity": adjusted_quantity,
        }

        trade_type = binance_account.type
        if trade_type == "S":
            client = Spot(api_key=binance_account.apiKey, api_secret=binance_account.secretKey)
            response = client.new_order(**order_params)
        elif trade_type == "U":
            client = UMFutures(key=binance_account.apiKey, secret=binance_account.secretKey)
            response = client.new_order(**order_params)
        elif trade_type == "C":
            client = CMFutures(key=binance_account.apiKey, secret=binance_account.secretKey)
            response = client.new_order(**order_params)
        else:
            raise ValueError("Invalid trade_type. Use 'spot', 'usdm', or 'coinm'.")

        return {
            "order_id": response["orderId"],
            "symbol": response["symbol"],
            "side": response["side"],
            "price": response.get("fills", [{}])[0].get("price", "0"),
            "quantity": response["origQty"],
        }
    
    except ClientError as e:
        raise ValueError(e.error_message)
    except Exception as e:
        raise ValueError(str(e))