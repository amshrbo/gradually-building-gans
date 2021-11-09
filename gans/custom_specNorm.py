import numpy as np

def l2_norm(x, w):
    '''
        Takes two args: 
            x: here it refer to (v or u)
            w: the weights matrix 
        Returns: the l2 norm of the mat x_w
    '''

    x_w = np.multiply(np.transpose(w), x)
    return np.linalg.norm(x_w)

def init_u(weights_shape):
    '''
        randomly initializes the U param from a random distribution
    '''

    print("--- initializing __u__")
    u_shape = weights_shape[0]
    print(f'The shape of u is : {u_shape}')
    u = np.random.randn(u_shape)

    return u



def compute_sn(weights, pow_itr):
    '''
        Input: 
            weights: a matrix of weights
            pow_itr: the number of times (u and v) gets updated 
        Outputs: a matrix of spectraly normalized weights
    '''
    # Initializing u
    u = init_u(weights.shape)
    u_updated = u

    for _ in range(pow_itr):
        # calculating U and V
        u_norm = l2_norm(u_updated, weights)
        v = np.multiply(np.transpose(weights), u_updated) / u_norm
        
        v_norm = l2_norm(v, weights)
        u_updated = np.multiply(weights, v) / v_norm


    # spectral normalizing weights
    sigma = np.multiply(np.transpose(u_updated), np.multiply(weights, v))
    w_spec_norm = np.divide(weights, sigma)

    return w_spec_norm



def main():
    weights = np.random.randn(5, 5)
    print(f"Weights initialized successfully: ")
    print(weights)
    print()

    sn_weights = compute_sn(weights, 1)

    print(f"\nThe values of the spectral normal weights are : ")
    print(sn_weights)


if __name__ == '__main__':
    main()