from datasets import Dataset
import os
import git
import tempfile

# List of repository URLs
repo_urls = ["https://github.com/joshcarp/evy-leetcode.git", "https://github.com/evylang/evy.git"]

# Function to find all ".evy" files in a repository and read their contents
def find_and_read_evy_files(repo_url):
    with tempfile.TemporaryDirectory() as tmp_dir:
        with git.Repo.clone_from(repo_url, os.path.join(tmp_dir, os.path.basename(repo_url))) as repo:
            evy_files = []
            evy_contents = []
            rows = []
            for root, dirs, files in os.walk(repo.working_dir):
                for file in files:
                    if file.endswith(".evy") or file.endswith(".md"):
                        file_path = os.path.join(root, file)
                        with open(file_path, "r") as f:
                            content = f.read()
                        file_path = os.path.join("data", os.path.basename(root), file)
                        os.makedirs(os.path.join("data", os.path.basename(root)), exist_ok=True)

                        with open(file_path, "w") as f:
                            f.write(content)
                        rows.append({"repo_url": repo_url, "file_path": file, "content": content})
    return rows
# Create the dataset
rows = []
for repo_url in repo_urls:
    rows.extend(find_and_read_evy_files(repo_url))
dataset = Dataset.from_list(rows)

import csv

# Save the dataset to a CSV file
# with open("evy_dataset.csv", "w", newline="") as csvfile:
#     fieldnames = ["repo_url", "file_path", "content"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for row in rows:
#         writer.writerow(row)

# Save the dataset to the Hugging Face Hub
# dataset.push_to_hub("joshcarp/evy-code")


