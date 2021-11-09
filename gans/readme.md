## Notes on the different implemenation of GAN

### Linear GAN
> Building a simple linear gan using only fully connected layers we get 

### Linear GAN with BatchNorm
> - Getting better result using BatchNorm weight normalization technique as the Gen loss dropped from `4.9 to 3.9` after only 20 epochs of training without doing hyperparam tunning 
> - Comparing this to the previous model (Linear GAN) we get a better result after all.

### DCGAN BatchNorm
> - Building a Convolutional GAN the loss dropped dastically from 3+ to 1+ and getting much better result.
> - _The discriminator_: here is less dominanet compared to the previous two models which gives the generator more room to learn and improve.

### DCGAN with SpectralNorm
> - The loss here is below 0.8 for both the __gen__ and the __disc__
> - The most obvious thing here is the both the gen adn disc get more compatitive, and this will lead to much better result after more (hyper-param tunning and training).
> - And also this compativness nature give us the ability to build more complex models in which we can use it for more complex datasets.
