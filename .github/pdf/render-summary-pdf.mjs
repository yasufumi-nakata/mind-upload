import { chromium } from "playwright";

async function main() {
  const [, , targetUrl, outputPath] = process.argv;

  if (!targetUrl || !outputPath) {
    throw new Error("Usage: node render-summary-pdf.mjs <url> <output-path>");
  }

  const browser = await chromium.launch({ headless: true });

  try {
    const page = await browser.newPage({
      viewport: { width: 1440, height: 2048 },
      deviceScaleFactor: 1
    });

    await page.goto(targetUrl, { waitUntil: "networkidle" });
    await page.waitForSelector(".summary-booklet-main", { state: "visible" });
    await page.emulateMedia({ media: "print" });
    await page.evaluate(async () => {
      if (document.fonts && document.fonts.ready) {
        await document.fonts.ready;
      }
    });

    await page.pdf({
      path: outputPath,
      format: "A4",
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: "<div></div>",
      footerTemplate: `
        <div style="width:100%; font-size:9px; color:#52606d; padding:0 12mm; display:flex; justify-content:space-between; font-family: 'Noto Sans JP', sans-serif;">
          <span>Mind-Upload Summary Booklet</span>
          <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
        </div>
      `,
      margin: {
        top: "16mm",
        right: "14mm",
        bottom: "18mm",
        left: "14mm"
      }
    });
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
