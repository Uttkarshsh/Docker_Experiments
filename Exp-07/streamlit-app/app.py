import os
from pathlib import Path
from typing import Dict, List, Text

import streamlit as st

from src.ui import (
    display_header,
    display_report,
    display_sidebar_header,
    select_period,
    select_project,
    select_report,
    set_page_container_style,
)
from src.utils import (
    EntityNotFoundError,
    get_reports_mapping,
    list_periods,
)

# Constants
PROJECTS_DIR: Path = Path("./projects")
REPORTS_DIR_NAME: Text = "reports"

def main():
    # Apply Streamlit style settings
    set_page_container_style()

    # Get project names
    projects: List[Text] = [p for p in os.listdir(PROJECTS_DIR) if not p.startswith(".")]

    try:
        # Sidebar UI elements
        display_sidebar_header()

        selected_project: Path = PROJECTS_DIR / select_project(projects)
        reports_dir: Path = selected_project / REPORTS_DIR_NAME

        periods: List[Text] = list_periods(reports_dir)
        selected_period: Text = select_period(periods)
        period_dir: Path = reports_dir / selected_period

        report_mapping: Dict[Text, Path] = get_reports_mapping(period_dir)
        selected_report_name: Text = select_report(report_mapping)
        selected_report: Path = report_mapping[selected_report_name]

        # Display selected report
        display_header(
            project_name=selected_project.name,
            period=selected_period,
            report_name=selected_report_name,
        )
        display_report(selected_report)

    except EntityNotFoundError as e:
        st.error(f"Error: {e}")

    except Exception as e:
        st.error("An unexpected error occurred.")
        st.exception(e)

if __name__ == "__main__":
    main()
