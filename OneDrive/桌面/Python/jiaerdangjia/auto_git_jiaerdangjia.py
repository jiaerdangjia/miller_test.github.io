import os
import subprocess

def copy_and_push(repo_path, folder_to_copy, commit_message, branch_name='master'):
    # Step 1: Copy the folder to the repository
    destination_path = os.path.join(repo_path, os.path.basename(folder_to_copy))
    subprocess.run(["xcopy", folder_to_copy, destination_path, "/E", "/H", "/K"], check=True)

    # Change directory to the repository
    os.chdir(repo_path)

    # Step 2: Add, commit to the local repository
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Step 3: Push to the remote repository
    subprocess.run(["git", "push", "origin", branch_name], check=True)

if __name__ == "__main__":
    # Example usage
    repo_path = r"C:\Users\mille\OneDrive\桌面\Python\jiaerdangjia"
    folder_to_copy = r"C:\Users\mille\OneDrive\桌面\Python\python\jiaerdangjia"
    commit_message = "ungrade"
    branch_name = "master"  # or "main" or any other branch

    copy_and_push(repo_path, folder_to_copy, commit_message, branch_name)