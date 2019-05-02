# GIT KPIs
There are four KPIs that software teams should track and improve to be a high performing team. These are lead time, mean time to restore, deployment frequency, and deployment failure rate. Please read [Accelerate](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339) by Nicole Forsgren PhD, Jez Humble, and Gene Kim for research.

There are much better tools than this for measuring these KPIs, like [GoCD](https://GoCD.org) that properly model the continuous delivery pipeline in a much better way. 

This application bridges the gap between having git tags and releases in GitHub, but not having a fully rolled out continuous delivery tool. 

So far this only tracks lead time for a given scenario. The definition of lead time here is the average time it takes from code commit to production. It assumes you tag at the time of pushing code to production. There are a number of assumptions here as it references the time of commits, which may not be the same as the time as things land on trunk. However, without instrumentation and process around specific commits, we can't get a better heuristic for time anyways, so hopefully commits themselves do not land too far away from when things are merged into trunk.

# Setup
For first-time setup, follow these steps:

1. Clone the repository
2. [Install poetry](https://github.com/sdispater/poetry#installation)
3. Ensure you have python 3.6 on your system. `brew install python` is one way. [pyenv](https://github.com/pyenv/pyenv) is another. Pick your favourite.
4. run `poetry install`
5. run `poetry shell`
6. run `pre-commit install` from within the shell
7. run tests with `pytest` from within the shell
8. run the cli tool with `metrics -h` to learn about its required arguments

# Example
Print lead time between releases with the key DLK
```bash
metrics --base v1.43 --head v1.43.7 --repository PyGithub/PyGithub --key Publish
```

# Fine print
There's some assumptions that need to hold true for this to work
* You must tag your releases
* Your commit messages must have some unique identifier or project tag to indicate work done