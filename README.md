# About

# Setup

Install following module.

- python 3.7
- pipenv

Then, Execute commands.

```
pipenv --python 3.7.2 
pipenv install
```

And make `api_key` file which is written your API KEY.

```
echo YOUR_API_KEY > api_key
```

# How to execute

Vision API samples are wrote in jupyter notebook. You can open notebook use `pipenv run jupyter` command.

## Description

- pre_trained_image_properties.ipynb
    - This script outputs API response of `IMAGE_PROPERTIES`
    - Plot color bar graph to notebook
- pre_trained_label_detection.ipynb
    - This script outputs API response of `LABEL_DETECTION`
    - Plot table of label
- pre_trained_web_detection.ipynb
    - This script outputs API response of `WEB_DETECTION`
    - Plot response image url to notebook
