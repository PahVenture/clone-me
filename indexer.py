import os
import yaml
import requests

def sanitize_text(text):
    """Sanitize text to avoid breaking Markdown table."""
    return text.replace('|', '&#124;').replace('\n', ' ').strip()

def update_directory():
    directory_path = 'directory'
    clones = []

    for filename in os.listdir(directory_path):
        if filename.startswith('@') and filename.endswith('.yaml'):
            with open(os.path.join(directory_path, filename), 'r') as file:
                clone_data = yaml.safe_load(file)
                if 'github_username' in clone_data:
                    try:
                        github_api_url = f"https://api.github.com/users/{clone_data['github_username']}"
                        response = requests.get(github_api_url)
                        
                        if response.status_code == 200:
                            user_data = response.json()
                            clone_data['github'] = clone_data.get('github', {})
                            clone_data['github'].update({
                                'avatar_url': user_data.get('avatar_url'),
                                'public_repos': user_data.get('public_repos'),
                                'followers': user_data.get('followers')
                            })
                        else:
                            raise Exception(f"Error occurred while fetching GitHub data: {response.status_code}")
                    except ImportError:
                        raise Exception("Warning: 'requests' library not installed. Skipping GitHub API validation.")
                    except Exception as e:
                        raise Exception(f"Error occurred while fetching GitHub data: {str(e)}")
                clones.append(clone_data)

    with open('DIRECTORY.md', 'w') as directory_file:
        directory_file.write("# Clone as Submodule and enjoy with your mentor or nemesis 💪\n\n")
        directory_file.write("```bash\n")
        directory_file.write("git submodule add git@github.com:username/clone-me.git .clone-me\n")
        directory_file.write("```\n\n")
        directory_file.write("# Directory of Clones\n\n")
        directory_file.write("| Name | GitHub | X | Description |\n")
        directory_file.write("|------|--------|---|-------------|\n")
        for clone in clones:
            name = sanitize_text(clone['name'])
            github = sanitize_text(clone.get('github_username', 'N/A'))
            x = sanitize_text(clone.get('x_username', 'N/A'))
            desc = sanitize_text(clone['description'])[:200]
            directory_file.write(f"| {name} | [{github}](https://github.com/{github}) | [{x}](https://twitter.com/{x}) | {desc} |\n")

if __name__ == "__main__":
    update_directory()