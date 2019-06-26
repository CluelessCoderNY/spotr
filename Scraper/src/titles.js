const puppeteer = require("puppeteer");

async function titles(page) {
  try {
    const selector = document.querySelector(
      "#sortable-results > .rows > .result-row:nth-child(1) > .result-info > .result-title"
    );

    const blah = await page.evaluate(selector => {
      document.querySelector(selector);
    }, selector);

    const rawTitles = await document.querySelector(
      'ul[class="rows"] > li > p a'
    ).innerText;

    const convertedTitles = Array.prototype.slice.call(rawTitles);

    const titles = convertedTitles.map(title => title);

    console.log(titles);
  } catch (err) {
    console.log("FUCK!", err);
  }
}

module.exports = titles;
