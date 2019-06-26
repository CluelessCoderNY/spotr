const puppeteer = require("puppeteer");
const postUrl = "https://newyork.craigslist.org/search/rva?postedToday=1";

const chooseTitle = async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto(postUrl, { waitUntil: "networkidle2" });

  try {
    const data = await page.evaluate(() => {
      const rawTitles = document.querySelectorAll(
        'a[class="result-title hdrlnk"]'
      );

      const convertedTitles = Array.prototype.slice.call(rawTitles);
      const titles = convertedTitles.map(title => title.innerText);

      return titles;
    });

    console.log(data.filter(x => x !== "#"));
  } catch (err) {
    console.log("fuck!", err);
  }

  // await browser.close();
};

chooseTitle();

module.exports = "chooseTitle";
