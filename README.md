# Stably Discordant Worker
Stably Discordant Worker is a python library for the client part of a client/server system. Drawing from my [Stable Discord](https://github.com/dankleeman/stable-discord/) project, the Stably Discordant project allows several machines to volunteer to contribute to a worker pool processing images. The distributed work is performed by a pool of workers (this project) that take commands from the control server. The server codebase can be found [here](https://github.com/dankleeman/stably-discordant-server/).

## Installation
Stably Discordant Server uses poetry to manage dependencies and installation.

**NOTE: Stably Discordant Server currently only supports python 3.10. While it is likely that some minor poetry work could easily extend this to other python versions, absolutely no testing or work has yet been performed to this end.**

### Linux / MacOS
A user may run the following steps manually or if they have `make` installed they may run `make setup`.

	python3 -m pip install poetry
	poetry install

### Windows
A user may run the following steps manually or if they have `make` installed they may run `make setup`.

	python3 -m pip install poetry
	poetry install
	poetry run pip install torch==1.13.1+cu117 -f https://download.pytorch.org/whl/torch_stable.html

**Note: I am not entirely clear on why the poetry install of torch fails to work correctly, but we can force poetry to use pip to grab wheels from the pytorch project directly.**

## Execution
Stably Discordant Worker may be started by running the `worker.py` file in the `app` directory of this repository: `poetrry run python app/server.py`. The worker accepts several command line arguments:
1. `--host-ip` (required) - provide the IP address of the control server host machine.
2. `--host-port` - provide the port for the control server. Defaults to `5556`.

**Note: Keep in mind that regular networking rules apply. If the server process is running on a local network and not all of the client machines are on that local network then some basic port forwarding may be in order.**
## Configuration with config.toml
Stably Discordant Worker is intended to localize all changes in the config.toml file.

### \[diffuser.settings\]
- `use_gpu` - A boolean flag indicating if the diffusion model should expect to use a GPU for accelerated processing. Defaults to `True`.
- `use_half_precision` - A boolean flag indicating if the diffusion model should use half precision floating point numbers. This will improve speed while reducing image quality. Defaults to `True`.
- `enable_xformers_attention` - A boolean flag indicating if the diffusion model should use the [xFormers](https://github.com/facebookresearch/xformers) library for accelerated attention. Defaults to `True`.
### \[misc_settings\]
- `log_dir`  - A path to the desired logging directory. Defaults to `logs`

## Contributing
This repository is open for use or to be forked freely. I intend to get Stably Discordant Worker to a stable state and leave it there, but I will consider contributions in the unlikely event they are provided.

## Changelog
See `CHANGELOG.md` file in the root directory of this repository. 

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
See the `LICENSE` file in the root directory of this repository. 

## Notes
### Conventions
README - https://www.makeareadme.com/

Semantic Versioning - https://semver.org/

### Other References
Licensing for Open Source: https://choosealicense.com/