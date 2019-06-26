const puppeteer = require("puppeteer");
const postUrl = "https://newyork.craigslist.org/search/rva?postedToday=1";

const choose = async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto(postUrl, { waitUntil: "networkidle2" });

  try {
    const data = await page.evaluate(() => {
      const rawTitles = document.querySelectorAll(
        'ul[class="rows"] > li > p a'
      );

      const convertedTitles = Array.prototype.slice.call(rawTitles);
      const titles = convertedTitles.map(title => title.innerText);

      const rawLinks = document.querySelectorAll('ul[class="rows"] > li > p a');

      const convertedLinks = Array.prototype.slice.call(rawLinks);
      const links = convertedLinks.map(title => title.getAttribute("href"));

      return {
        titles,
        links
      };
    });

    console.log(data);
  } catch (err) {
    console.log("fuck!", err);
  }

  // await browser.close();
};

choose();

// const puppeteer = require("puppeteer");
// const postUrl = "https://newyork.craigslist.org/search/rva?postedToday=1";

// const choose = async () => {
//   const browser = await puppeteer.launch({ headless: false });
//   const page = await browser.newPage();
//   await page.goto(postUrl, { waitUntil: "networkidle2" });

//   const data = await page.evaluate(() => {
//     const rawLinks = document.querySelectorAll('ul[class="rows"] > li > p a');

//     const convertedLinks = Array.prototype.slice.call(rawLinks);
//     const links = convertedLinks.map(title => title.getAttribute("href"));

//     return links;
//   });

//   console.log(data.filter(x => x !== "#"));

//   // await browser.close();
// };

// choose();
