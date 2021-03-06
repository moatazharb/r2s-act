R2S-ACT FAQ
============

This is a list of Frequently Asked Questions about R2S-ACT.

How do I...
-----------
... make my MOAB mesh file viewable in VisIT?
   Use `mbconvert mesh.h5m mesh.vtk` to convert .h5m files to .vtk files, which can be loaded into VisIT

... easily run different photon calculations (e.g. biased and unbiased) from the same neutron calculation?
   You can have different `r2s.cfg` files and pass them to the setup scripts, e.g.

        `r3s-act/scripts/r2s_step2.py r2s.cfg_1`

... setup calculations for photon transport for several cooling steps?
   The script `r2s_step2setup.py` can be run once ALARA has been run.
   This script will create folders for each cooling step, and copy the mesh, MCNP input (for photons) and `r2s.cfg` files.

... tag custom photon energy bins to my mesh?
   Copy and modify `r2s-act/scripts/tools/tag_ebins.py`

... tag bias factors to my mesh?
   Copy and modify `r2s-act/scripts/tools/tag_bias_example.py`

More questions
--------------
What should I do if I want to ensure zero activation in a region?
   If the region is, e.g. air, one option is set the density of the material to zero in the `matlib` file.

   Another scenario this arises in is if the MCNP models for neutron and photon transport differ, then an activation calculation using the 'photon' geometry can be done.
   Counter-intuitively, this is done by specifying the photon input file in the 'neutron_mcnp_input' entry in your `r2s.cfg` file.

If the parameter 'u' or 'v' is switched to 'v' or 'u' (respectively) in a `gammas` file, results are very different!?
    To change sampling approach, the `gammas` file needs to be regenerated by modifying `r2s.cfg` accordingly, and running `r2s_step2.py` again.

    The reason for this is that the `gammas` file values are preprocessed; in particular, for voxel sampling, entries are voxel *source strengths*, while for uniform sampling, entries are *source densities*.
