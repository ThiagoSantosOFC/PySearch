from github import Github

ACCESS_TOKEN = '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'

g = Github(ACCESS_TOKEN)


def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')

    print(f'Found {result.totalCount} repo(s)')

    for repo in result:
        print(f'{repo.clone_url}, {repo.stargazers_count} stars')


if __name__ == '__main__':
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    search_github(keywords)
