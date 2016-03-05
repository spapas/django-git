import git

r = git.Repo('..')
print r.git.log(pretty='{hash:"%H", subject:"%s", commiter_date:"%cd"}', n=1, date='format:%Y-%m-%d:%H:%M%S')