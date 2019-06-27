// const puppeteer = require("puppeteer");
// const postUrl = "https://newyork.craigslist.org/search/rva?postedToday=1";

const getTitles = async () => {
  const browser = await puppeteer.launch({ headless: true });
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

    console.log(data);
  } catch (err) {
    console.log("oops!", err);
  }

  await browser.close();
};

getTitles();

module.exports = "getTitles";
