# Contributing to the Cookbook

Do you want to contribute an example to the cookbook? We currently support **four categories of examples**:

- [**Machine Learning Descriptors**](descriptors.md): Examples of how to construct descriptors from raw data.
- [**Machine Learning Models**](models.md): Using raw data or descriptors, how to construct a (typically supervised regression) model.
- [**Data Analysis**](analysis.md): Using raw data or descriptors, how to construct a (typically unsupervised) ML analysis.
- [**Publications**](publications.md): Full or partial workflows from prior established studies.

In these categories, you can choose one of **two example types**:

- **Linked example**: Link to another repository containing your example
- **Hosted example**: Upload your notebook, a list of requirements, and the necessary inputs to the cookbook. Notebook should run on the supported python versions using the requirements provided.

**If your example takes more than 2 minutes to run, we require that you provide a companion testing script.**

## Linked example:

1. Make a folder in the `examples` folder for your example.
2. In this folder provide a `meta.json` that contains the following items:
  - ``title``: title of the example
  - ``author``: name of the author of the example
  - ``author_email``: email of the author of the example
  - ``category``: {``descriptors``, ``models``, ``analysis``, or ``publications``}
  - ``icon``: (optional) name or url of the image to use for the TOC grid. If none is provided, we will use the lab-COSMO logo.
  - ``link``: url of the example
3. Push your example to a new branch called `addition/{your-example-name}` and [submit a pull request](https://github.com/bananenpampe/COSMO_cookbook/pulls).

You're all set! We will regularly check that the url provided remains active, and will ping the `author_email` should the url return a reference error.

## Hosted example:

1. Make a folder in the `examples` folder for your example.
2. In this folder, provide a `requirements.txt` that contains the pip dependencies of the example.
3. Move your examples into your folder -- make sure they include a top-level title so that they show up in the Table of Contents.
4. In this folder, provide a `meta.json` that contains the following items:
      - ``title``: title of the example
      - ``author``: name of the author of the example
      - ``author_email``: email of the author of the example
      - ``category``: {``descriptors``, ``models``, ``analysis``, or ``publications``}
      - ``files``: list of file names (referential names within the folder) of the pages to display
      - ``icon``: (optional) name or url of the image to use for the TOC grid. If none is provided, we will use the lab-COSMO logo.
      - ``test_cmd``: (optional) bash command to run the tests for your example. If this is not provided, we will test all entries in ``files`` using `python` and `jupyter nbconvert`, as appropriate.
5. Push your example to a new branch called `addition/{your-example-name}` and [submit a pull request](https://github.com/bananenpampe/COSMO_cookbook/pulls).


You're all set! We will regularly run the tests provided, and will ping the `author_email` should they return an error.
