import pytest
from datetime import datetime
import os


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the Pytest HTML report to include screenshots on failure.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Check if the 'page' fixture is available in the test
        page = item.funcargs.get("page")
        if page:
            # Ensure the directory exists
            screenshot_dir = "test_results/screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            # Create a unique filename
            file_name = f"fail_{item.name}_{datetime.now().strftime('%H%M%S')}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            # Take the screenshot
            page.screenshot(path=file_path)

            # Add the screenshot to the HTML report
            if file_path:
                html = '<div><img src="screenshots/%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
