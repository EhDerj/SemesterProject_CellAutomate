cd ./src/modules/view

# Init
pybabel init -i view.pot -D view -d ./locales -l ru

# Compile
pybabel compile -D view -d ./locales -l ru
