import argparse
import os
import re
from pathlib import Path
import json # Added for debugging if needed, not strictly used in final script logic

# Team names and their corresponding section headings in the daily files
TEAM_HEADINGS = {
    "Team 1": "## Team 1",
    "Team 2": "## Team 2",
    "Team 3": "## Team 3",
    "Learning Hour": "## Learning Hour"
}

def get_daily_status_files(source_dir):
    """Finds all YYYY-MM-DD.md files in the source directory."""
    files = []
    source_path = Path(source_dir)
    if not source_path.is_dir():
        print(f"Error: Source directory '{source_path.resolve()}' does not exist or is not a directory.")
        return files

    for entry in source_path.iterdir():
        if entry.is_file() and re.match(r"\d{4}-\d{2}-\d{2}\.md", entry.name):
            files.append(entry)
    files.sort() # Process in chronological order
    return files

def extract_section_content(file_path, section_heading):
    """Extracts content under a specific section heading from a file."""
    content = []
    in_section = False
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith(section_heading):
                    in_section = True
                    continue
                if in_section:
                    # Stop if we hit another major heading (## or #)
                    if line.startswith("## ") or line.startswith("# "):
                        break
                    content.append(line)
    except FileNotFoundError:
        # This case should ideally be handled by checking file existence before calling
        print(f"Warning: File not found {file_path} (should not happen if get_daily_status_files is robust)")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

    return "".join(content).strip() if content else None


def main():
    parser = argparse.ArgumentParser(description="Compiles content for a specific team/part from daily status files.")
    parser.add_argument("part_name", choices=list(TEAM_HEADINGS.keys()), 
                        help="The name of the team or part to compile (e.g., 'Team 1', 'Learning Hour').")
    parser.add_argument("--source_dir", default=".", 
                        help="Directory containing the daily status (YYYY-MM-DD.md) files. Defaults to current directory.")
    parser.add_argument("--output_dir", default=".", 
                        help="Directory to save the compiled <part_name>.complete.md file. Defaults to current directory.")

    args = parser.parse_args()

    target_heading = TEAM_HEADINGS[args.part_name]
    
    # Sanitize part_name for use in filename (replace spaces, etc.)
    safe_part_name_for_file = args.part_name.replace("/", "_") 
    output_file_path = Path(args.output_dir) / f"{safe_part_name_for_file}.complete.md"

    try:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True) # Ensure output directory exists
    except Exception as e:
        print(f"Error creating output directory {args.output_dir}: {e}")
        return

    daily_files = get_daily_status_files(args.source_dir)
    
    source_dir_resolved = Path(args.source_dir).resolve()

    if not daily_files:
        message = f"No daily status files (YYYY-MM-DD.md) found in '{source_dir_resolved}'."
        print(message)
        # Create an empty file as per "Create a <part>.complete.md file for each part."
        try:
            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                outfile.write(f"# {args.part_name} - Compiled Report\n\n")
                outfile.write(f"{message}\n")
            print(f"Empty compiled report (due to no daily files) saved to {output_file_path}")
        except Exception as e:
            print(f"Error writing empty report to {output_file_path}: {e}")
        return

    found_any_content = False

    print(f"Found the following {len(daily_files)} daily file(s) in '{source_dir_resolved}':")
    for i, daily_file in enumerate(daily_files, 1):
        print(f"  {i}. {daily_file.name}")
    print(f"\nProcessing for part '{args.part_name}' (looking for heading: '{target_heading}')...")

    compiled_content_parts = []
    for daily_file in daily_files:
        # print(f"  Processing {daily_file.name}...") # Verbose
        section_text = extract_section_content(daily_file, target_heading)
        if section_text:
            compiled_content_parts.append(f"## From {daily_file.name}\n\n{section_text}\n")
            found_any_content = True
        # else:
            # print(f"    Section '{target_heading}' not found or empty in {daily_file.name}.") # Verbose

    # Add a Key section placeholder as per the process document, regardless of content found
    key_section = (
        "# Key\n"
        "-  <p style=\"background-color: yellow\">Pattern 1</p>\n"
        "-  <p style=\"background-color: lightgreen\">Pattern 2</p>\n\n"
    )
    
    final_output_content = key_section

    if not found_any_content:
        message = f"No content found for '{args.part_name}' (heading: '{target_heading}') in any of the {len(daily_files)} daily file(s) processed in '{source_dir_resolved}'."
        print(message)
        final_output_content += f"# {args.part_name} - Compiled Report\n\n"
        final_output_content += f"{message}\n"
    else:
        full_compiled_text = "\n".join(compiled_content_parts)
        final_output_content += full_compiled_text

    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.write(final_output_content)
        if not found_any_content:
            print(f"Compiled report with no specific content for '{args.part_name}' saved to {output_file_path}")
        else:
            print(f"Successfully compiled content for '{args.part_name}' into {output_file_path}")
    except Exception as e:
        print(f"Error writing to output file {output_file_path}: {e}")

if __name__ == "__main__":
    main()
