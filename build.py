import os
import json
import shutil
import subprocess

from jinja2 import Environment, FileSystemLoader

# Check if dist folder exists. If it does, delete contents; otherwise, create.
directory = "./dist/"
if os.path.exists(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
else:
    try:
        os.mkdir("./dist/")
    except OSError:
        print ("Creation of the directory failed")
        exit()

# Required for jinja
template_env = Environment(
    loader=FileSystemLoader('./templates/')
)

post_names = os.listdir('posts/')
posts = []

for post in post_names:
    with open('posts/' + post + '/data.json') as f:
        d = json.load(f)
    posts.append(d)

# Create blog homepage
index_template = template_env.get_template('index.html')
with open('dist/index.html', 'w') as f:
    f.write(index_template.render(posts=posts))

# Create each post
post_template = template_env.get_template('post.html')
for post in posts:
    nb = 'posts/' + post['id'] + '/content.ipynb'
    p = subprocess.Popen(['jupyter', 'nbconvert', '--to=html', '--template=templates/custom.tpl', nb])
    p.communicate()
    with open('posts/' + post['id'] + '/content.html') as f:
        content = f.read()
    with open('dist/' + post['id'] + '.html', 'w') as f:
        f.write(post_template.render(post=post, content=content))
    if os.path.exists('posts/' + post['id'] + '/content.html'):
        os.remove('posts/' + post['id'] + '/content.html')

# Copy assets
shutil.copytree('assets/', 'dist/assets/')
