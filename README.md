# kaist_tpu
Instructions for create_tpu_v3:
```
1. `pip install fire`
1. install gcloud via https://cloud.google.com/sdk/docs/install
3. run `gcloud init` with zone `europe-west4-a`
```

## Flops:
```
1x v3-8 ~ 492 teraflops
1x V100 ~ 130 teraflops
1x A100 ~ 312 teraflops
8x V100 ~ 1040 teraflops
5x v3-8 ~ 2460 teraflops
8x A100 ~ 2496 teraflops
```

## Useful links:
- https://github.com/huggingface/transformers/tree/main/examples/flax/language-modeling
