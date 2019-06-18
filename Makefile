
run:
	ls tests | xargs -I '{}' -n 1 python ./s.py cursed tests/{} output/{}
	gio open output/
