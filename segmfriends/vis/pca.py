import numpy as np
from sklearn.decomposition import PCA


def pca(embedding, output_dimensions=3, reference=None, center_data=False):
    # embedding shape: first two dimensions corresponde to batchsize and embedding dim, so
    # shape should be (B, E, H, W) or (B, E, D, H, W).
    _pca = PCA(n_components=output_dimensions)
    # reshape embedding
    output_shape = list(embedding.shape)
    output_shape[1] = output_dimensions
    flat_embedding = embedding.reshape(embedding.shape[0], embedding.shape[1], -1)
    flat_embedding = flat_embedding.transpose((0, 2, 1))
    if reference is not None:
        # assert reference.shape[:2] == embedding.shape[:2]
        flat_reference = reference.reshape(reference.shape[0], reference.shape[1], -1)\
            .transpose((0, 2, 1))
    else:
        flat_reference = flat_embedding

    if center_data:
        means = np.mean(flat_reference, axis=0, keepdims=True)
        flat_reference -= means
        flat_embedding -= means

    pca_output = []
    for flat_reference, flat_image in zip(flat_reference, flat_embedding):
        # fit PCA to array of shape (n_samples, n_features)..
        _pca.fit(flat_reference)
        # ..and apply to input data
        pca_output.append(_pca.transform(flat_image))

    return np.stack([x.T for x in pca_output]).reshape(output_shape)

if __name__ == '__main__':
    print(pca(np.random.rand(2, 64, 20, 100, 100)).shape)
