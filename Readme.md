# Compare Image Api

CompareImageApi is a Python API for comparing two images if they're the same.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

Install [FastAPI](https://fastapi.tiangolo.com/)

```bash
pip install fastapi
pip install uvicorn
```

```bash
pip install opencv-python
pip install numpy
pip install pydantic
pip install scikit-image
```

## Run

```bash
uvicorn main:app --reload
```

## Example

```bash
curl --location 'http://127.0.0.1:8000/compareImage' \
--header 'Content-Type: application/json' \
--data '{
    "source": "## main image",
    "template": "## image to compare",
    "threshold": 0.6
}'
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
