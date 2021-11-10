## Notes on the different implemenation of GAN
> Note That I've used the mentioned pytorch example, and built the models gradually over it

___NOTES:___    
- I Didn't manage to implement a full working version of specNorm to work with pytorch 
- So I implemented a [___simpler numpy version of the spectral normalization algorithm.___](./custom_specNorm.py) Based on my understanding after skimming the paper and after reading the mentioned code example.
- I used the mentioned specNorm implementation of pytorch to be able to integrate it with my model.

__Spectral normalization algorithm steps:__
1. __Randomly initialize U_hat__
2. __Calculate V_hat as follows:__ `v_hat = (Trans(W) * u_hat) / l2_norm(Trans(W) * u_hat)`
3. __Update U_hat as follows:__ `u_hat = (W * v_hat) / l2_norm(W * v_hat)`
4. __Repeat__ `2 and 3` __for the required power_iterations__
5. __Calculate Sigma as follows:__ `sigma = Trans(u_hat) * W * v_hat`
6. __Spectral normalized Weight:__ `W_spec_norm = W/sigma`


### Linear GAN
> Building a simple linear gan using only fully connected layers we got terrible results and the model have +4 as loss for the generator 

### Linear GAN with BatchNorm
> - Getting better result using BatchNorm weight normalization technique as the Gen loss dropped from `4.9 to 3.9` after only 20 epochs of training without doing hyperparam tunning 
> - Comparing this to the previous model (Linear GAN) we get a better result after all.

### DCGAN with BatchNorm
> - Building a Convolutional GAN the loss dropped drastically from 3+ to 1+ and getting much better result.
> - _The discriminator_: here is less dominanet compared to the previous two models which gives the generator more room to learn and improve.

### DCGAN with SpectralNorm
> - The loss here is below 0.8 for both the __gen__ and the __disc__
> - The most obvious thing here is the both the gen adn disc get more compatitive, and this will lead to much better result after more (hyper-param tunning and training).
> - And also this compativness nature give us the ability to build more complex models in which we can use it for more complex datasets.

