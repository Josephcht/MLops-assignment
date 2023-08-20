
# MLops Assignment

Prediction of HDB resale price and Cardiovascular issue using machine learning models and using it in a website deployed for prediciton.
## Why?
It is important to structure your data science project based on a certain standard so that your teammates can easily maintain and modify your project.

## Tools used in this project
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/2023/06/12/poetry-a-better-way-to-manage-python-dependencies/)
* [hydra](https://hydra.cc/): Manage configuration files - [article](https://mathdatasimplified.com/2023/05/25/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting
* [DVC](https://dvc.org/): Data version control - [article](https://mathdatasimplified.com/2023/02/20/introduction-to-dvc-data-version-control-tool-for-machine-learning-projects-2/)
* [pdoc](https://github.com/pdoc3/pdoc): Automatically create an API documentation for your project

## Project Structure
```bash
.
├── config                      
│   ├── config.yaml           # Second variation of parameters to process data                    
├── notebooks                              # store notebooks
    ├── 201423L_MLOpsAssignment_v2.ipynb   # Nicole's EDA and modelling
    └── 210893L EDA and Modelling.ipynb    # Joseph's EDA and modelling
├── README.md                              # describe your project and File structure
├── Dockerfile                             # Dockerfile for deployment
├── Procfile                               # for deployment
├── requirements.txt                       # Versions of the libraries that we used
├── src                                    # store source code
│   ├── 201423L_MLOps_Final.pkl            # Nicole's saved model
│   ├── final_model_lightgbm.pkl           # Joseph's saved model
│   ├── app.py                             # Main flask app
│   ├── Forms.py                           # Forms that we used
│   └── wsgi.py                            # calling from app.py for no hard coding
└── templates                              # store html files
    ├── includes
        └── _formHelper.html               
    ├── base.html                          # base html that all html files uses
    ├── pred.html                          # Nicole's Form for prediction
    └── prediction.html                    # Joseph's Form for prediction
```



