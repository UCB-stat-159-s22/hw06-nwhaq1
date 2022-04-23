# creates and configures the conda environment.

.PHONY: env
env:
	bash -i setup.sh
	pip install .

# build the JupyterBook normally (calling jupyterbook build .). Note this build can only be viewed if the repo is cloned locally, # or with the VNC desktop on the hub.

.PHONY: html
html :
	jupyter-book build .
    
# build the JupyterBook so that you can view it on the hub with the URL proxy trick as indicated above.

.PHONY: html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html && python -m http.server
 

# build the JupyterBook so that you can view it on the hub with the URL proxy trick as indicated above.
.PHONY: clean
clean:
	rm -r figures
	rm -r audio
	mkdir figures
	cd figures && touch .gitkeep
	mkdir audio
	cd audio && touch .gitkeep