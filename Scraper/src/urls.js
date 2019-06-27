const puppeteer = require("puppeteer");

const getUrls = async postUrl => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(postUrl, { waitUntil: "networkidle2" });

  const linkData = await page.evaluate(() => {
    const rawLinks = document.querySelectorAll('ul[class="rows"] > li > p a');
    const convertedLinks = Array.prototype.slice.call(rawLinks);
    const links = convertedLinks.map(title => title.getAttribute("href"));
    const filteredLinks = links.filter(x => x !== "#");

    return filteredLinks;
  });

  console.log("job completed");

  await browser.close();

  return linkData;
};

module.exports = getUrls;
