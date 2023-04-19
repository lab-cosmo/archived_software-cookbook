COSMO Software Cookbook
=======================


.. include:: ../../README.rst
   :start-after: marker-intro
   :end-before: marker-building

.. toctree::
  :maxdepth: 1
  :caption: Contents:

  tutorials


Some example

.. jupyter-execute::

    import ipywidgets as w
    from IPython.display import display

    a = w.IntSlider()
    b = w.IntText()
    w.jslink((a, 'value'), (b, 'value'))
    display(a, b)
