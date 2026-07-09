import json
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
from django.core.cache import cache
from django.shortcuts import render


def projects_view(request):
    github_username = 'Dikashyanta'

    repos = cache.get('github_repos')
    if not repos:
        quoted_username = quote(github_username, safe='')
        url = (
            f'https://api.github.com/users/{quoted_username}/repos?'
            + urlencode({'sort': 'updated', 'per_page': 12})
        )
        github_request = Request(url, headers={'User-Agent': 'personal-site'})
        try:
            with urlopen(github_request) as response:
                repos = json.loads(response.read().decode())
        except (HTTPError, URLError, json.JSONDecodeError):
            repos = []

        cache.set('github_repos', repos, timeout=60 * 30)  # cache 30 min

    return render(request, 'project/project.html', {
        'repos': repos,
        'github_username': github_username,
    })
