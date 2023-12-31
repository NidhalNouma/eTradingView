function swapDivBtn(id1, id2) {
  const btn1 = document.getElementById(id1 + "-btn");
  const btn2 = document.getElementById(id2 + "-btn");
  const div1 = document.getElementById(id1);
  const div2 = document.getElementById(id2);

  const btnClass1 = btn1.classList.toString(); // Convert class list to string
  const btnClass2 = btn2.classList.toString(); // Convert class list to string

  btnClass1.split(" ").forEach((className) => {
    btn1.classList.remove(className);
  });

  btnClass2.split(" ").forEach((className) => {
    btn2.classList.remove(className);
  });

  btnClass1.split(" ").forEach((className) => {
    btn2.classList.add(className);
  });

  btnClass2.split(" ").forEach((className) => {
    btn1.classList.add(className);
  });

  div1.classList.add("hidden");
  div2.classList.remove("hidden");
}

function openLoader(title, id = "-pay-submit-") {
  document.getElementById("spinner" + id + title).style.display = "block";
  document.getElementById("btn" + id + title).style.display = "none";

  if (document.getElementById("error" + id + title))
    document.getElementById("error" + id + title).style.display = "none";
}
function closeLoader(title, id = "-pay-submit-") {
  document.getElementById("spinner" + id + title).style.display = "none";
  document.getElementById("btn" + id + title).style.display = "block";

  if (document.getElementById("error" + id + title))
    document.getElementById("error" + id + title).style.display = "none";
}
function closeLoader(title, id = "-pay-submit-") {
  document.getElementById("spinner" + id + title).style.display = "none";
  document.getElementById("btn" + id + title).style.display = "block";
}
function changeHidden(id1, id2) {
  document.getElementById(id1)?.classList?.remove("hidden");
  document.getElementById(id2)?.classList?.add("hidden");
}

function customDropdownBtnClick(newValue, textId, inputId, buttonId) {
  const text = document.getElementById(textId);
  const input = document.getElementById(inputId);
  const btn = document.getElementById(buttonId);
  if (text) text.innerText = newValue;
  if (input) input.value = newValue;
  if (btn) btn.click();
}

function validateNumberInput(input, maxLength) {
  let value = input.value.replace(/\D/g, "").slice(0, maxLength);

  let formattedValue = "";

  for (let i = 0; i < value.length; i++) {
    if (i > 0 && i % 4 === 0) {
      formattedValue += " ";
    }
    formattedValue += value[i];
  }

  input.value = formattedValue.trim();
}

let stripe, cardElement, elements;

function mountStripeElement(id) {
  if (!stripe) {
    stripe = Stripe(
      "pk_test_51NQMS2J5gHo8PE1NkuozkIhIpTZ04rH9zWLHdqqFwSTTPG3ciGfylBLolIdsaYnddawM6sN55JmoTuJCNjEQO4ST00JFXmLBeR"
    );
    elements = stripe.elements();
    cardElement = elements.create("card", {
      hidePostalCode: true,
      style: {
        base: {
          color: "#fff",
          "font-size": "0.875rem",
          "line-height": "1.25rem",

          iconColor: "rgb(156 163 175)",
          "::placeholder": {
            color: "rgb(156 163 175)",
          },
          ":focus": {
            "border-color": "rgb(63 131 248);",
          },
        },
      },
    });
  }

  cardElement.mount("#card-element-" + id);
}

function unmountStripeElement(title) {
  cardElement.unmount();
  closeLoader(title);
}

function paymentMethodSelected(pmId, inputId) {
  const pmValue = document.getElementById(inputId);

  document
    .getElementById("span-" + pmValue.value + "-" + inputId)
    ?.classList?.add("hidden");
  document
    .getElementById("span-" + pmId + "-" + inputId)
    ?.classList?.remove("hidden");

  pmValue.value = pmId;
}

async function onPayFormStripeSubmit(title) {
  openLoader(title);
  const nameInput = document.getElementById("cardName-" + title);

  const pmValue = document.getElementById("pm-" + title);

  if (pmValue.value.length === 0) {
    const result = await stripe.createPaymentMethod({
      elements,
      params: {
        billing_details: {
          name: nameInput.value,
        },
      },
    });
    if (result.error) {
      console.log(`Payment failed: ${result.error.message}`);
      closeLoader(title);
      return false;
    } else {
      console.log(result);

      pmValue.value = result.paymentMethod.id;
    }
  }

  let form = document.getElementById("form-pay-" + title);
  form.dispatchEvent(new Event("submit"));

  // closeLoader(title);
  return true;
}

//Hide css element after fadeout
function hideAll_hideMe() {
  const elements = document.querySelectorAll(".hideMe");
  // console.log("running", elements);

  elements.forEach(function (element) {
    element.addEventListener("animationend", function () {
      element.classList.add("hidden");
      // console.log(element);
    });
  });
}

hideAll_hideMe();

// Show/Hide replies

function toggleReplies(id) {
  const replies = document.getElementById("replies-" + id);
  const upArrow = document.getElementById("up-arrow-replies-" + id);
  const dnArrow = document.getElementById("down-arrow-replies-" + id);
  if (replies.classList.contains("hidden")) {
    replies.classList.remove("hidden");
    upArrow.classList.remove("hidden");
    dnArrow.classList.add("hidden");
  } else {
    replies.classList.add("hidden");
    dnArrow.classList.remove("hidden");
    upArrow.classList.add("hidden");
  }
}

function toggleForm(btnId, formId, textFocus = true) {
  const btn = document.getElementById(btnId);
  const form = document.getElementById(formId);
  if (btn && form)
    if (form.classList.contains("hidden")) {
      form.classList.remove("hidden");
      btn.classList.add("hidden");

      if (textFocus) {
        let firstTextField = form.querySelector("textarea");
        if (firstTextField) {
          firstTextField.focus();
        }
      }
    } else {
      form.classList.add("hidden");
      btn.classList.remove("hidden");
    }
}

function showSelectImgs(id) {
  const input = document.getElementById(id);
  input.click();
}

function showModalImages(images, imgId, id = "modal-images") {
  // console.log(images);
  const modal = document.getElementById(id);
  modal.classList.remove("hidden");

  let currentIndex = 0;

  const showImage = (index) => {
    const carouselItems = carouselContainer.querySelectorAll(
      "[data-carousel-item]"
    );
    carouselItems.forEach((item, i) => {
      item.style.display = i === index ? "block" : "none";
    });

    currentIndex = index;
  };

  document
    .getElementById("prev-button-carousel")
    .addEventListener("click", () => {
      currentIndex = (currentIndex - 1 + images.length) % images.length;
      showImage(currentIndex);
    });

  document
    .getElementById("next-button-carousel")
    .addEventListener("click", () => {
      currentIndex = (currentIndex + 1) % images.length;
      showImage(currentIndex);
    });

  const carouselControl = document.getElementById("controls-carousel");
  const carouselContainer = document.getElementById("images-carousel");
  while (carouselContainer.firstChild) {
    carouselContainer.removeChild(carouselContainer.firstChild);
  }

  images.forEach((img, index) => {
    console.log(img);
    const imgElement = document.createElement("img");
    imgElement.src = img.imageUrl;
    imgElement.classList.add(
      "object-scale-down",
      "absolute",
      "max-w-[95%]",
      "max-h-[99%]",
      "aspect-auto",
      "block",
      "-translate-x-1/2",
      "-translate-y-1/2",
      "top-1/2",
      "left-1/2"
    );

    const carouselItem = document.createElement("div");
    carouselItem.classList.add("hidden", "duration-700", "ease-in-out");
    carouselItem.setAttribute("data-carousel-item", "");
    carouselItem.appendChild(imgElement);

    carouselContainer.appendChild(carouselItem);

    if (img.id == imgId) {
      showImage(index);
    }
  });
}

htmx.on("htmx:afterRequest", (evt) => {
  if (evt?.detail?.target.id === "settingsDiv") {
    clearResultForm();
  }

  if (evt?.detail?.target.id.includes("form-pay-")) {
    const title = evt?.detail?.target.id.replace("form-pay-", "");
    mountStripeElement(title);
  }

  if (evt?.detail?.target.id.includes("stripe-error-")) {
    const title = evt?.detail?.target.id.replace("stripe-error-", "");
    closeLoader(title);
  }

  if (evt?.detail?.target.id === "setting-payment_methods") {
    const closeForm = document.getElementById(
      "add-payment_methods-close-form-btn"
    );
    closeForm.click();
  }
  // check which element triggered the htmx request. If it's the one you want call the function you need
  //you have to add htmx: before the event ex: 'htmx:afterRequest'
});

function scrollToResult(resultId) {
  const resultElement = document.getElementById(`result-${resultId}`);

  if (resultElement) {
    // Calculate the scroll position to center the element
    const windowHeight = window.innerHeight;
    const elementTop = resultElement.getBoundingClientRect().top;
    const offset = elementTop - windowHeight / 2;

    // Scroll to the element
    window.scrollTo({
      top: window.scrollY + offset,
      behavior: "smooth",
    });

    // Add a highlight class
    resultElement.classList.add("brightness-125");
    resultElement.classList.add("transition");
    resultElement.classList.add("ease-in-out");
    resultElement.classList.add("duration-1000");

    // Remove the highlight after a certain time (e.g., 3 seconds)
    setTimeout(() => {
      resultElement.classList.remove("brightness-125");
      // resultElement.classList.remove("transition");
      // resultElement.classList.remove("ease-in-out");
      // resultElement.classList.remove("duration-1000");
    }, 3000);
  }
}

function handleSettingCsvFileSelect(event) {
  const fileInput = event.target;
  const file = fileInput.files[0];

  if (!file) {
    return;
  }

  const reader = new FileReader();

  reader.onload = function (e) {
    const contents = e.target.result;
    const lines = contents.split("\n");

    let previousKey = "";
    lines.forEach((line, index) => {
      let [key, value] = line.split(",");

      value = value.replace(/(\r\n|\n|\r)/gm, "");
      key = key.replace(/(\r\n|\n|\r)/gm, "");

      if (key.length === 0) key = previousKey + "_val";

      const input = document.getElementById("id_settings_" + key);
      if (input && input.type == "checkbox") {
        if (value === "On") {
          input.checked = true;
          input.value = "true";
        } else {
          input.checked = false;
          input.value = "false";
        }
      } else if (input && input.type == "text") {
        input.value = value;

        const dropdown = document.getElementById("dropdown_text_" + key);
        if (dropdown) dropdown.innerHTML = value;
      }

      if (key === "Symbol" && document.getElementById("pair")) {
        const [broker, symbol] = value.split(":");
        document.getElementById("pair").value = symbol;
        document.getElementById("broker").value = broker;
      } else if (key === "Trading range") {
        const [start, end] = value.split(" — ");

        if (document.getElementById("start_at")) {
          const time = new Date(start);
          time.setMinutes(time.getMinutes() - time.getTimezoneOffset());
          document.getElementById("start_at").value = time
            .toISOString()
            .slice(0, 16);
        }
        if (document.getElementById("end_at")) {
          const time = new Date(end);
          time.setMinutes(time.getMinutes() - time.getTimezoneOffset());
          document.getElementById("end_at").value = time
            .toISOString()
            .slice(0, 16);
        }
      } else if (key === "Timeframe") {
        const [num, str] = value.split(" ");

        if (document.getElementById("time_frame"))
          document.getElementById("time_frame").value = num;
        if (document.getElementById("time_frame_period")) {
          const val = str.replace(/(\r\n|\n|\r)/gm, "");
          document.getElementById("time_frame_period").value = val;
        }
      } else if (key === "Initial capital") {
        if (document.getElementById("initial_capital"))
          document.getElementById("initial_capital").value = value;
      }

      previousKey = key;
    });

    fileInput.value = null;
  };

  reader.readAsText(file);
}

function handleResultsCsvFileSelect(event) {
  const fileInput = event.target;
  const file = fileInput.files[0];

  if (!file) {
    return;
  }

  const reader = new FileReader();

  reader.onload = function (e) {
    const contents = e.target.result;
    const lines = contents.split("\n");

    let previousKey = "";
    lines.forEach((line, index) => {
      let [key, allUSD, allPerc, longUSD, longPerc, shortUSD, shortPerc] =
        line.split(",");

      key = key.replace(/(\r\n|\n|\r)/gm, "");
      allUSD = allUSD.replace(/(\r\n|\n|\r)/gm, "");
      allPerc = allPerc.replace(/(\r\n|\n|\r)/gm, "");
      longUSD = longUSD.replace(/(\r\n|\n|\r)/gm, "");
      longPerc = longPerc.replace(/(\r\n|\n|\r)/gm, "");
      shortUSD = shortUSD.replace(/(\r\n|\n|\r)/gm, "");
      shortPerc = shortPerc.replace(/(\r\n|\n|\r)/gm, "");

      if (key === "Net Profit") {
        if (document.getElementById("net_profit"))
          document.getElementById("net_profit").value = allUSD;
        if (document.getElementById("net_profit_long"))
          document.getElementById("net_profit_long").value = longUSD;
        if (document.getElementById("net_profit_short"))
          document.getElementById("net_profit_short").value = shortUSD;
        if (document.getElementById("net_profit_percentage"))
          document.getElementById("net_profit_percentage").value = allPerc;
        if (document.getElementById("net_profit_percentage_long"))
          document.getElementById("net_profit_percentage_long").value =
            longPerc;
        if (document.getElementById("net_profit_percentage_short"))
          document.getElementById("net_profit_percentage_short").value =
            shortPerc;
      } else if (key === "Gross Profit") {
        if (document.getElementById("gross_profit"))
          document.getElementById("gross_profit").value = allUSD;
        if (document.getElementById("gross_profit_long"))
          document.getElementById("gross_profit_long").value = longUSD;
        if (document.getElementById("gross_profit_short"))
          document.getElementById("gross_profit_short").value = shortUSD;
        if (document.getElementById("gross_profit_percent"))
          document.getElementById("gross_profit_percent").value = allPerc;
        if (document.getElementById("gross_profit_percent_long"))
          document.getElementById("gross_profit_percent_long").value = longPerc;
        if (document.getElementById("gross_profit_percent_short"))
          document.getElementById("gross_profit_percent_short").value =
            shortPerc;
      } else if (key === "Gross Loss") {
        if (document.getElementById("gross_loss"))
          document.getElementById("gross_loss").value = allUSD;
        if (document.getElementById("gross_loss_long"))
          document.getElementById("gross_loss_long").value = longUSD;
        if (document.getElementById("gross_loss_short"))
          document.getElementById("gross_loss_short").value = shortUSD;
        if (document.getElementById("gross_loss_percent"))
          document.getElementById("gross_loss_percent").value = allPerc;
        if (document.getElementById("gross_loss_percent_long"))
          document.getElementById("gross_loss_percent_long").value = longPerc;
        if (document.getElementById("gross_loss_percent_short"))
          document.getElementById("gross_loss_percent_short").value = shortPerc;
      } else if (key === "Profit Factor") {
        if (document.getElementById("profit_factor"))
          document.getElementById("profit_factor").value = allUSD;
        if (document.getElementById("profit_factor_long"))
          document.getElementById("profit_factor_long").value = longUSD;
        if (document.getElementById("profit_factor_short"))
          document.getElementById("profit_factor_short").value = shortUSD;
      } else if (key === "Percent Profitable") {
        if (document.getElementById("profitable_percentage"))
          document.getElementById("profitable_percentage").value = allUSD;
        if (document.getElementById("profitable_percentage_long"))
          document.getElementById("profitable_percentage_long").value = longUSD;
        if (document.getElementById("profitable_percentage_short"))
          document.getElementById("profitable_percentage_short").value =
            shortUSD;
      } else if (key === "Max Drawdown") {
        if (document.getElementById("max_dd"))
          document.getElementById("max_dd").value = allUSD;
        if (document.getElementById("max_dd_percentage"))
          document.getElementById("max_dd_percentage").value = allPerc;
      } else if (key === "Total Closed Trades") {
        if (document.getElementById("total_trades"))
          document.getElementById("total_trades").value = allUSD;
        if (document.getElementById("total_trades_long"))
          document.getElementById("total_trades_long").value = longUSD;
        if (document.getElementById("total_trades_short"))
          document.getElementById("total_trades_short").value = shortUSD;
      } else if (key === "Number Winning Trades") {
        if (document.getElementById("winning_trades"))
          document.getElementById("winning_trades").value = allUSD;
        if (document.getElementById("winning_trades_long"))
          document.getElementById("winning_trades_long").value = longUSD;
        if (document.getElementById("winning_trades_short"))
          document.getElementById("winning_trades_short").value = shortUSD;
      } else if (key === "Number Losing Trades") {
        if (document.getElementById("losing_trades"))
          document.getElementById("losing_trades").value = allUSD;
        if (document.getElementById("losing_trades_long"))
          document.getElementById("losing_trades_long").value = longUSD;
        if (document.getElementById("losing_trades_short"))
          document.getElementById("losing_trades_short").value = shortUSD;
      }
    });

    fileInput.value = null;
  };

  reader.readAsText(file);
}

function getNumberOfLines(id) {
  const element = document.getElementById(id);
  let lineHeight = parseFloat(window.getComputedStyle(element).lineHeight);
  let totalHeight = element.scrollHeight;
  // console.log(totalHeight, totalHeight / lineHeight);
  return Math.round(totalHeight / lineHeight);
}

const modals = {};
function openModel(id) {
  const modalElement = document.querySelector("#" + id);

  const modalOptions = {
    // placement: "bottom-right",
    // backdrop: "dynamic",
    // backdropClasses: "bg-gray-900/50 dark:bg-gray-900/80 fixed inset-0 z-40",
    // onHide: () => {
    //   console.log("modal is hidden");
    // },
    // onShow: () => {
    //   console.log("modal is shown");
    // },
    // onToggle: () => {
    //   console.log("modal has been toggled");
    // },
  };

  if (modals[id]) modals[id].show();
  else {
    const modal = new Modal(modalElement, modalOptions);
    modals[id] = modal;
    modal.show();
  }
}

function hideModel(id) {
  if (modals[id]) modals[id].hide();
}
