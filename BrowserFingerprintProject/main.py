"""
Main Application Entry Point
Browser Fingerprinting Detection and Prevention System
"""

import sys
from playwright.sync_api import sync_playwright


def main():
    print("[*] Starting Browser Fingerprinting Detection & Prevention System...")
    print("[*] Launching installed Google Chrome via Playwright...")

    with sync_playwright() as p:
        try:
            # channel="chrome" targets the user's installed Google Chrome browser
            browser = p.chromium.launch(
                channel="chrome",
                headless=False,
            )
            context = browser.new_context()
            page = context.new_page()

            target_url = "https://example.com"
            print(f"[*] Navigating to {target_url}...")
            page.goto(target_url, wait_until="domcontentloaded")

            title = page.title()
            current_url = page.url

            print("\n" + "=" * 50)
            print(f"[+] Website Title : {title}")
            print(f"[+] Website URL   : {current_url}")
            print("=" * 50 + "\n")

            page.wait_for_timeout(2000)
            print("[*] Closing browser safely...")
            context.close()
            browser.close()
            print("[+] Browser closed successfully. Test completed.")
        except Exception as e:
            print(f"[-] Error occurred: {e}", file=sys.stderr)
            raise


if __name__ == "__main__":
    main()
