.PHONY: all clean_env build_image run_container

clean_env:
	-docker rm -f app-py
build_image:
	docker build -t app-py .
run_container:
	docker run -d --name app-py -p 5000:5000 app-py
all: clean_env build_image run_container