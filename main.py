from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

GITHUB_API_URL = "https://api.github.com"

@app.delete("/delete-repo/")
def delete_repo(owner: str, repo: str, pat: str):
    """
    Delete a GitHub repository using a PAT.
    Params:
      - owner: GitHub username/org name
      - repo: Repository name
      - pat: Personal Access Token
    """
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        return {"message": f"Repository {owner}/{repo} deleted successfully."}
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Repository not found or access denied.")
    else:
        raise HTTPException(status_code=response.status_code, detail=response.json())
