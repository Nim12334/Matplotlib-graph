import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.close("all")
a= np.random.gamma(12,2.2,12)
print(a)



df5 = pd.DataFrame(
    {
        "a":np.random.binomial(0,0.0001,1000) ,
        "b": np.random.gumbel(0,0.0001,1000),
        "c": np.random.gumbel(0,0.0001,1000),
    },
    columns=["a", "b", "c"],
)

plt.figure()

df5.plot.hist(alpha=1)
plt.show()