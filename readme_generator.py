import os

def optional_input(prompt):
    response = input(prompt)
    return response.strip() if response.strip() else None

def generate_readme():
    print("Welcome to the detailed README generator!")
    project_name = input("Enter the project name: ")
    description = input("Enter a detailed project description: ")
    features = optional_input("Enter key features of the project (comma separated, or leave blank): ")
    installation = optional_input("Enter installation instructions (or leave blank): ")
    usage = optional_input("Enter usage information (or leave blank): ")
    contributing = optional_input("Enter contributing guidelines (or leave blank): ")
    tests = optional_input("Enter test instructions (or leave blank): ")
    badges = optional_input("Enter any badge markdown you want to include at the top (or leave blank): ")
    license_name = optional_input("Enter license (e.g., MIT) or leave blank: ")
    author = input("Enter author name: ")
    github_username = optional_input("Enter GitHub username for contact link (or leave blank): ")
    email = optional_input("Enter email for contact (or leave blank): ")

    readme_content = f"""
# {project_name}
"""

    if badges:
        readme_content += f"\n{badges}\n"

    readme_content += f"""
## Description

{description}
"""

    if features:
        feature_list = features.split(",")
        readme_content += "\n## Features\n\n"
        for feat in feature_list:
            readme_content += f"- {feat.strip()}\n"

    if installation:
        readme_content += f"\n## Installation\n\n{installation}\n"

    if usage:
        readme_content += f"\n## Usage\n\n{usage}\n"

    if contributing:
        readme_content += f"\n## Contributing\n\n{contributing}\n"

    if tests:
        readme_content += f"\n## Tests\n\n{tests}\n"

    if license_name:
        readme_content += f"\n## License\n\nThis project is licensed under the {license_name} License.\n"

    readme_content += "\n---\n\n"
    readme_content += f"*Author: {author}*\n"

    if github_username or email:
        readme_content += "\n## Contact\n\n"
        if github_username:
            readme_content += f"- GitHub: [@{github_username}](https://github.com/{github_username})\n"
        if email:
            readme_content += f"- Email: {email}\n"

    with open("README.md", "w") as f:
        f.write(readme_content)

    print("README.md file generated successfully with detailed sections!")

if __name__ == "__main__":
    generate_readme()
