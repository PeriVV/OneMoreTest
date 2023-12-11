
## Evaluation Results

The evaluation results are presented in the first five columns of Table. The second column specifies the error rates of the selected methods.  Columns 3-5  specify how many testing items ranked in the top k (k=1,  10, and 100, respectively) by OneMoreTest are fault-revealing.  The last two rows present the precision and recall of the evaluated approaches. 
<table>
  <tr>
    <th rowspan="2">ID</th>
    <th rowspan="2">Error Rate</th>
    <th colspan="3">OneMoreTest</th>
    <th colspan="3">Random Selection</th>
    <th colspan="3">Coverage-based Selection</th>
    <th colspan="3">Invariant-based Selection</th>
  </tr>
  <tr>
    <th>Top1</th>
    <th>Top10</th>
    <th>Top100</th>
    <th>Top1</th>
    <th>Top10</th>
    <th>Top100</th>
    <th>Top1</th>
    <th>Top10</th>
    <th>Top100</th>
    <th>Top1</th>
    <th>Top10</th>
    <th>Top100</th>
  </tr>
<tr>
    <td>M1</td><td>20%</td><td>1</td><td>10</td><td>100</td><td>0.32</td><td>2.12</td><td>19.84</td><td>0.19</td><td>2.15</td><td>20.52</td><td>0.15</td><td>1.82</td><td>19.17</td>
</tr>
<tr>
    <td>M2</td><td>34.53%</td><td>1</td><td>10</td><td>100</td><td>0.36</td><td>3.47</td><td>35.22</td><td>0.3</td><td>5.49</td><td>38.22</td><td>0.5</td><td>5</td><td>49.66</td>
</tr>
<tr>
    <td>M3</td><td>49.99%</td><td>1</td><td>10</td><td>100</td><td>0.62</td><td>4.93</td><td>49.68</td><td>0.54</td><td>4.98</td><td>49.67</td><td>0.4</td><td>3.19</td><td>34.5</td>
</tr>
<tr>
    <td>M4</td><td>25.37%</td><td>1</td><td>10</td><td>100</td><td>0.21</td><td>2.54</td><td>24.75</td><td>0.27</td><td>3.41</td><td>26.54</td><td>0.61</td><td>4.92</td><td>50.73</td>
</tr>
<tr>
    <td>M5</td><td>5.18%</td><td>1</td><td>10</td><td>100</td><td>0.05</td><td>0.49</td><td>5.25</td><td>0.1</td><td>0.57</td><td>9.29</td><td>0.24</td><td>2.7</td><td>25.36</td>
</tr>
<tr>
    <td>M6</td><td>23.61%</td><td>1</td><td>10</td><td>100</td><td>0.51</td><td>5.17</td><td>49.69</td><td>0.26</td><td>5.73</td><td>55.28</td><td>0.06</td><td>0.54</td><td>5.08</td>
</tr>
<tr>
    <td>M7</td><td>4.37%</td><td>1</td><td>10</td><td>100</td><td>0.07</td><td>0.29</td><td>4.34</td><td>0.26</td><td>2.43</td><td>24.56</td><td>0.56</td><td>5.17</td><td>49.98</td>
</tr>
<tr>
    <td>M8</td><td>9%</td><td>1</td><td>10</td><td>100</td><td>0.11</td><td>0.85</td><td>8.53</td><td>0.55</td><td>5.69</td><td>75.19</td><td>0.53</td><td>5.19</td><td>50.33</td>
</tr>
<tr>
    <td>M9</td><td>3.92%</td><td>1</td><td>10</td><td>100</td><td>0.06</td><td>0.29</td><td>3.92</td><td>0.16</td><td>2.89</td><td>7.21</td><td>0.28</td><td>2.44</td><td>24.99</td>
</tr>
<tr>
    <td>M10</td><td>53.20%</td><td>1</td><td>10</td><td>100</td><td>0.6</td><td>5.21</td><td>52.34</td><td>0.47</td><td>5.21</td><td>50.59</td><td>0.74</td><td>7.32</td><td>75.38</td>
</tr>
<tr>
    <td>M11</td><td>34.53%</td><td>1</td><td>10</td><td>100</td><td>0.36</td><td>3.47</td><td>35.22</td><td>0.25</td><td>5.78</td><td>39.44</td><td>0</td><td>0</td><td>0</td>
</tr>
<tr>
    <td>M12</td><td>49.99%</td><td>1</td><td>10</td><td>100</td><td>0.62</td><td>4.93</td><td>49.68</td><td>0.78</td><td>5.89</td><td>58</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M13</td><td>0.98%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.13</td><td>1.06</td><td>0</td><td>0.1</td><td>0.97</td><td>0.01</td><td>0.09</td><td>0.93</td>
</tr>
<tr>
    <td>M14</td><td>0.99%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.11</td><td>0.92</td><td>0.02</td><td>0.11</td><td>1.06</td><td>0.02</td><td>0.11</td><td>0.99</td>
</tr>
<tr>
    <td>M15</td><td>0.96%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.08</td><td>0.96</td><td>0.01</td><td>0.12</td><td>0.97</td><td>0.01</td><td>0.08</td><td>0.87</td>
</tr>
<tr>
    <td>M16</td><td>1.01%</td><td>1</td><td>10</td><td>100</td><td>0.04</td><td>0.63</td><td>6.59</td><td>0.01</td><td>0.53</td><td>6.37</td><td>0.1</td><td>0.55</td><td>6.55</td>
</tr>
<tr>
    <td>M17</td><td>39.99%</td><td>1</td><td>10</td><td>100</td><td>0.37</td><td>4.34</td><td>39.85</td><td>0.34</td><td>4.12</td><td>40.96</td><td>0.24</td><td>3.07</td><td>30.16</td>
</tr>
<tr>
    <td>M18</td><td>59%</td><td>1</td><td>10</td><td>100</td><td>0.6</td><td>5.76</td><td>59.16</td><td>0.12</td><td>2.02</td><td>60.03</td><td>0.1</td><td>0.3</td><td>10.2</td>
</tr>
<tr>
    <td>M19</td><td>39.55%</td><td>1</td><td>10</td><td>100</td><td>0.36</td><td>3.96</td><td>39.72</td><td>0.42</td><td>3.84</td><td>39.95</td><td>0.44</td><td>3.86</td><td>40.28</td>
</tr>
<tr>
    <td>M20</td><td>1.81%</td><td>1</td><td>10</td><td>100</td><td>0.02</td><td>0.19</td><td>1.76</td><td>0.02</td><td>0.24</td><td>1.95</td><td>0.51</td><td>4.04</td><td>39.67</td>
</tr>
<tr>
    <td>M21</td><td>21.04%</td><td>1</td><td>10</td><td>100</td><td>0.23</td><td>2.12</td><td>20.58</td><td>0.46</td><td>4.85</td><td>25.58</td><td>0.02</td><td>0.17</td><td>1.82</td>
</tr>
<tr>
    <td>M22</td><td>6.74%</td><td>1</td><td>10</td><td>100</td><td>0.11</td><td>0.68</td><td>6.7</td><td>0.25</td><td>2.87</td><td>62.31</td><td>0.13</td><td>2.12</td><td>21.03</td>
</tr>
<tr>
    <td>M23</td><td>78%</td><td>1</td><td>10</td><td>100</td><td>0.78</td><td>7.1</td><td>76</td><td>1</td><td>10</td><td>100</td><td>0.49</td><td>4.83</td><td>49.26</td>
</tr>
<tr>
    <td>M24</td><td>0.29%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.32</td><td>1</td><td>0.01</td><td>0.53</td><td>6.37</td><td>0.1</td><td>0.55</td><td>6.55</td>
</tr>
<tr>
    <td>M25</td><td>7%</td><td>1</td><td>10</td><td>100</td><td>0.05</td><td>0.69</td><td>7.02</td><td>0.11</td><td>0.8</td><td>7.27</td><td>0.02</td><td>0.6</td><td>6.2</td>
</tr>
<tr>
    <td>M26</td><td>2.69%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.34</td><td>2.76</td><td>0.13</td><td>2.42</td><td>29.5</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M27</td><td>0.22%</td><td>1</td><td>10</td><td>100</td><td>0</td><td>0.02</td><td>0.15</td><td>1</td><td>10</td><td>100</td><td>0.42</td><td>4.59</td><td>49.31</td>
</tr>
<tr>
    <td>M28</td><td>0.22%</td><td>1</td><td>10</td><td>100</td><td>0</td><td>0.02</td><td>0.15</td><td>0</td><td>0.01</td><td>0.15</td><td>0.59</td><td>4.87</td><td>50.55</td>
</tr>
<tr>
    <td>M29</td><td>8.35%</td><td>1</td><td>10</td><td>100</td><td>0.06</td><td>0.81</td><td>8.13</td><td>0.59</td><td>5.01</td><td>49.35</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M30</td><td>49.97%</td><td>1</td><td>10</td><td>100</td><td>0.45</td><td>4.94</td><td>49.53</td><td>0.55</td><td>5.46</td><td>59.82</td><td>0.55</td><td>5</td><td>49.57</td>
</tr>
<tr>
    <td>M31</td><td>53.66%</td><td>1</td><td>10</td><td>100</td><td>0.53</td><td>5.36</td><td>53.66</td><td>0.78</td><td>8.45</td><td>66.34</td><td>0.39</td><td>3.72</td><td>35.37</td>
</tr>
<tr>
    <td>M32</td><td>8.35%</td><td>1</td><td>10</td><td>100</td><td>0.06</td><td>0.81</td><td>8.13</td><td>1</td><td>10</td><td>100</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M33</td><td>2.01%</td><td>1</td><td>10</td><td>100</td><td>0.05</td><td>0.23</td><td>2.18</td><td>0.03</td><td>0.27</td><td>2.32</td><td>0.45</td><td>4.9</td><td>50.99</td>
</tr>
<tr>
    <td>M34</td><td>8.35%</td><td>1</td><td>10</td><td>100</td><td>0.06</td><td>0.81</td><td>8.13</td><td>0.08</td><td>0.92</td><td>8.15</td><td>0.5</td><td>5.09</td><td>51.01</td>
</tr>
<tr>
    <td>M35</td><td>50%</td><td>1</td><td>10</td><td>100</td><td>0.43</td><td>4.81</td><td>50.18</td><td>0.47</td><td>5.21</td><td>50.59</td><td>0.6</td><td>6.05</td><td>59.97</td>
</tr>
<tr>
    <td>M36</td><td>44.39%</td><td>1</td><td>10</td><td>100</td><td>0.33</td><td>3.65</td><td>34.05</td><td>0.36</td><td>3.52</td><td>35.23</td><td>0.09</td><td>1.71</td><td>16.41</td>
</tr>
<tr>
    <td>M37</td><td>50.07%</td><td>1</td><td>10</td><td>100</td><td>0.52</td><td>5.31</td><td>50.17</td><td>0.5</td><td>4.98</td><td>49.79</td><td>0</td><td>0</td><td>0</td>
</tr>
<tr>
    <td>M38</td><td>49.95%</td><td>1</td><td>10</td><td>100</td><td>0.63</td><td>6.01</td><td>59.47</td><td>0.65</td><td>6.07</td><td>60.41</td><td>0.56</td><td>5.82</td><td>55.39</td>
</tr>
<tr>
    <td>M39</td><td>16.70%</td><td>1</td><td>10</td><td>100</td><td>0.11</td><td>1.56</td><td>16.7</td><td>0.14</td><td>1.59</td><td>16.19</td><td>0.46</td><td>5.17</td><td>50.72</td>
</tr>
<tr>
    <td>M40</td><td>49.00%</td><td>1</td><td>10</td><td>100</td><td>0.49</td><td>4.15</td><td>48.87</td><td>0.61</td><td>6.24</td><td>52.35</td><td>0.51</td><td>4.55</td><td>45.73</td>
</tr>
<tr>
    <td>M41</td><td>8.10%</td><td>1</td><td>10</td><td>100</td><td>0.08</td><td>0.81</td><td>8.34</td><td>0.2</td><td>2.9</td><td>11.82</td><td>0.03</td><td>0.3</td><td>3.16</td>
</tr>
<tr>
    <td>M42</td><td>4.13%</td><td>1</td><td>10</td><td>100</td><td>0</td><td>0.41</td><td>4</td><td>0.12</td><td>2.5</td><td>7.48</td><td>1</td><td>9.99</td><td>99.88</td>
</tr>
<tr>
    <td>M43</td><td>99.08%</td><td>1</td><td>10</td><td>100</td><td>0.9</td><td>9</td><td>99</td><td>1</td><td>10</td><td>100</td><td>0.98</td><td>9.84</td><td>98.58</td>
</tr>
<tr>
    <td>M44</td><td>1.44%</td><td>1</td><td>10</td><td>100</td><td>0.02</td><td>0.15</td><td>1.44</td><td>0.14</td><td>2.24</td><td>4.92</td><td>0.54</td><td>4.79</td><td>50.49</td>
</tr>
<tr>
    <td>M45</td><td>0.97%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.07</td><td>1</td><td>0.13</td><td>2.16</td><td>4.48</td><td>0.47</td><td>4.28</td><td>9.94</td>
</tr>
<tr>
    <td>M46</td><td>9.64%</td><td>1</td><td>10</td><td>100</td><td>0.1</td><td>0.96</td><td>9.84</td><td>0.22</td><td>3.05</td><td>13.32</td><td>0.56</td><td>5.17</td><td>18.78</td>
</tr>
<tr>
    <td>M47</td><td>25.05%</td><td>1</td><td>10</td><td>100</td><td>0.21</td><td>2.4</td><td>25.13</td><td>0.33</td><td>4.49</td><td>28.61</td><td>0.67</td><td>6.61</td><td>34.07</td>
</tr>
<tr>
    <td>M48</td><td>9.64%</td><td>1</td><td>10</td><td>100</td><td>0.08</td><td>0.81</td><td>8.34</td><td>0.2</td><td>2.9</td><td>11.82</td><td>0.54</td><td>5.02</td><td>17.28</td>
</tr>
<tr>
    <td>M49</td><td>22.22%</td><td>1</td><td>10</td><td>100</td><td>0.21</td><td>2.38</td><td>22.54</td><td>0.33</td><td>4.47</td><td>26.02</td><td>0.67</td><td>6.59</td><td>31.48</td>
</tr>
<tr>
    <td>M50</td><td>3.84%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.35</td><td>4.24</td><td>0.13</td><td>2.44</td><td>7.72</td><td>0.47</td><td>4.56</td><td>13.18</td>
</tr>
<tr>
    <td>M51</td><td>0.97%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.07</td><td>1</td><td>0.13</td><td>2.16</td><td>4.48</td><td>0.47</td><td>4.28</td><td>9.94</td>
</tr>
<tr>
    <td>M52</td><td>1.44%</td><td>1</td><td>10</td><td>100</td><td>0.02</td><td>0.15</td><td>1.44</td><td>0.14</td><td>2.24</td><td>4.92</td><td>0.48</td><td>4.36</td><td>10.38</td>
</tr>
<tr>
    <td>M53</td><td>25.05%</td><td>1</td><td>10</td><td>100</td><td>0.32</td><td>2.47</td><td>24.91</td><td>0.44</td><td>4.56</td><td>28.39</td><td>0.78</td><td>6.68</td><td>33.85</td>
</tr>
<tr>
    <td>M54</td><td>38.70%</td><td>1</td><td>10</td><td>100</td><td>0.38</td><td>3.83</td><td>38.56</td><td>0.49</td><td>5.17</td><td>42.61</td><td>0.83</td><td>7.29</td><td>48.07</td>
</tr>
<tr>
    <td>M55</td><td>8.35%</td><td>1</td><td>10</td><td>100</td><td>0.14</td><td>0.9</td><td>7.86</td><td>0.25</td><td>2.24</td><td>11.91</td><td>0.59</td><td>4.36</td><td>17.37</td>
</tr>
<tr>
    <td>M56</td><td>21.04%</td><td>1</td><td>10</td><td>100</td><td>0.42</td><td>3.76</td><td>38.96</td><td>0.53</td><td>5.1</td><td>43.01</td><td>0.87</td><td>7.22</td><td>67.35</td>
</tr>
<tr>
    <td>M57</td><td>1.68%</td><td>1</td><td>10</td><td>100</td><td>0.02</td><td>0.19</td><td>1.76</td><td>0.13</td><td>1.53</td><td>5.81</td><td>0.47</td><td>3.65</td><td>30.15</td>
</tr>
<tr>
    <td>M58</td><td>5.18%</td><td>1</td><td>10</td><td>100</td><td>0.05</td><td>0.49</td><td>5.25</td><td>0.16</td><td>1.83</td><td>9.3</td><td>0.5</td><td>3.95</td><td>33.64</td>
</tr>
<tr>
    <td>M59</td><td>98.08%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.14</td><td>1.52</td><td>0.1</td><td>1.48</td><td>5.57</td><td>0.44</td><td>2.04</td><td>29.91</td>
</tr>
<tr>
    <td>M60</td><td>33.30%</td><td>1</td><td>10</td><td>100</td><td>0.06</td><td>0.86</td><td>8.5</td><td>0.12</td><td>2.2</td><td>12.55</td><td>0.46</td><td>1.69</td><td>36.89</td>
</tr>
<tr>
    <td>M61</td><td>3.84%</td><td>1</td><td>10</td><td>100</td><td>0</td><td>0.28</td><td>2.9</td><td>0.11</td><td>0.84</td><td>6.95</td><td>0.45</td><td>2.41</td><td>31.29</td>
</tr>
<tr>
    <td>M62</td><td>33.30%</td><td>1</td><td>10</td><td>100</td><td>0.3</td><td>3.4</td><td>33</td><td>0.32</td><td>3.96</td><td>37.05</td><td>0.66</td><td>1.05</td><td>61.39</td>
</tr>
<tr>
    <td>M63</td><td>8.35%</td><td>1</td><td>10</td><td>100</td><td>0.06</td><td>0.71</td><td>7.4</td><td>0.09</td><td>1.27</td><td>11.45</td><td>0.43</td><td>4.17</td><td>35.79</td>
</tr>
<tr>
    <td>M64</td><td>21.04%</td><td>1</td><td>10</td><td>100</td><td>0.22</td><td>2.1</td><td>21.04</td><td>0.35</td><td>2.66</td><td>25.09</td><td>0.56</td><td>1.48</td><td>49.43</td>
</tr>
<tr>
    <td>M65</td><td>29.08%</td><td>1</td><td>10</td><td>100</td><td>0.3</td><td>3</td><td>29.08</td><td>0.35</td><td>3.56</td><td>33.13</td><td>0.56</td><td>2.87</td><td>57.47</td>
</tr>
<tr>
    <td>M66</td><td>0.99%</td><td>1</td><td>10</td><td>100</td><td>0</td><td>0.01</td><td>0.99</td><td>0.31</td><td>0.57</td><td>5.04</td><td>0.52</td><td>3.77</td><td>29.38</td>
</tr>
<tr>
    <td>M67</td><td>9.09%</td><td>1</td><td>10</td><td>100</td><td>0.09</td><td>0.9</td><td>9.09</td><td>0.17</td><td>1.46</td><td>13.14</td><td>0.38</td><td>0.78</td><td>40.03</td>
</tr>
<tr>
    <td>M68</td><td>29.35%</td><td>1</td><td>10</td><td>100</td><td>0.22</td><td>2.95</td><td>29.35</td><td>0.22</td><td>3.51</td><td>33.4</td><td>0.43</td><td>1.67</td><td>60.29</td>
</tr>
<tr>
    <td>M69</td><td>40.26%</td><td>1</td><td>10</td><td>100</td><td>0.36</td><td>3.86</td><td>39.68</td><td>0.36</td><td>4.42</td><td>43.73</td><td>0.57</td><td>3.72</td><td>70.62</td>
</tr>
<tr>
    <td>M70</td><td>0.99%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.07</td><td>0.85</td><td>0.03</td><td>1.1</td><td>10.86</td><td>0.24</td><td>4.63</td><td>37.75</td>
</tr>
<tr>
    <td>M71</td><td>9.09%</td><td>1</td><td>10</td><td>100</td><td>0.09</td><td>0.9</td><td>9.09</td><td>0.08</td><td>0.8</td><td>9.01</td><td>0.29</td><td>1.31</td><td>35.9</td>
</tr>
<tr>
    <td>M72</td><td>0.69%</td><td>1</td><td>10</td><td>100</td><td>0</td><td>0.05</td><td>0.77</td><td>0.02</td><td>2.06</td><td>5.78</td><td>0.23</td><td>4.15</td><td>32.67</td>
</tr>
<tr>
    <td>M73</td><td>9.08%</td><td>1</td><td>10</td><td>100</td><td>0.09</td><td>0.9</td><td>9.09</td><td>0.09</td><td>0.93</td><td>9.16</td><td>0.3</td><td>3.02</td><td>36.05</td>
</tr>
<tr>
    <td>M74</td><td>20.92%</td><td>1</td><td>10</td><td>100</td><td>0.22</td><td>2.1</td><td>21.04</td><td>0.17</td><td>1.97</td><td>21.11</td><td>0.38</td><td>4.06</td><td>48</td>
</tr>
<tr>
    <td>M75</td><td>7.69%</td><td>1</td><td>10</td><td>100</td><td>0.06</td><td>0.71</td><td>7.4</td><td>0.06</td><td>0.9</td><td>7.97</td><td>0.27</td><td>2.99</td><td>34.86</td>
</tr>
<tr>
    <td>M76</td><td>33.30%</td><td>1</td><td>10</td><td>100</td><td>0.22</td><td>2.95</td><td>29.35</td><td>0.29</td><td>5.13</td><td>89.71</td><td>0.32</td><td>7.22</td><td>97.23</td>
</tr>
<tr>
    <td>M77</td><td>99%</td><td>1</td><td>10</td><td>100</td><td>0.9</td><td>9</td><td>99</td><td>1</td><td>10</td><td>100</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M78</td><td>97.05%</td><td>1</td><td>10</td><td>100</td><td>1</td><td>10</td><td>100</td><td>0.32</td><td>9.71</td><td>97.23</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M79</td><td>53%</td><td>1</td><td>10</td><td>100</td><td>0.58</td><td>5.3</td><td>55.73</td><td>0.56</td><td>5.34</td><td>55.74</td><td>0.54</td><td>7.43</td><td>47.69</td>
</tr>
<tr>
    <td>M80</td><td>29.35%</td><td>1</td><td>10</td><td>100</td><td>0.22</td><td>2.95</td><td>29.35</td><td>0.16</td><td>3.85</td><td>40.84</td><td>0.54</td><td>5.94</td><td>50.49</td>
</tr>
<tr>
    <td>M81</td><td>0.99%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.07</td><td>0.85</td><td>0.01</td><td>0.5</td><td>5.45</td><td>0.74</td><td>7.66</td><td>78</td>
</tr>
<tr>
    <td>M82</td><td>9.09%</td><td>1</td><td>10</td><td>100</td><td>0.09</td><td>0.9</td><td>9.09</td><td>0.08</td><td>1.04</td><td>9.54</td><td>0.25</td><td>2.35</td><td>22.18</td>
</tr>
<tr>
    <td>M83</td><td>0.69%</td><td>1</td><td>10</td><td>100</td><td>0.21</td><td>2.15</td><td>21.33</td><td>0.13</td><td>2.23</td><td>21.13</td><td>0.25</td><td>2.46</td><td>25.4</td>
</tr>
<tr>
    <td>M84</td><td>9.08%</td><td>1</td><td>10</td><td>100</td><td>0.11</td><td>0.67</td><td>7.51</td><td>0.06</td><td>0.67</td><td>7.74</td><td>0.35</td><td>4.1</td><td>38.75</td>
</tr>
<tr>
    <td>M85</td><td>20.92%</td><td>1</td><td>10</td><td>100</td><td>0.23</td><td>2.23</td><td>21.19</td><td>0.28</td><td>4.76</td><td>25.04</td><td>0.88</td><td>9.21</td><td>92.45</td>
</tr>
<tr>
    <td>M86</td><td>7.69%</td><td>1</td><td>10</td><td>100</td><td>0.11</td><td>0.67</td><td>7.69</td><td>0.31</td><td>3.16</td><td>29.87</td><td>0.39</td><td>0.39</td><td>38.36</td>
</tr>
<tr>
    <td>M87</td><td>33.30%</td><td>1</td><td>10</td><td>100</td><td>0.33</td><td>3.33</td><td>33.3</td><td>0.35</td><td>7.76</td><td>97.04</td><td>1</td><td>9.99</td><td>99.88</td>
</tr>
<tr>
    <td>M88</td><td>99%</td><td>1</td><td>10</td><td>100</td><td>1</td><td>10</td><td>100</td><td>1</td><td>10</td><td>100</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M89</td><td>29.35%</td><td>1</td><td>10</td><td>100</td><td>0.22</td><td>2.95</td><td>29.35</td><td>0.22</td><td>2.74</td><td>28.44</td><td>0.44</td><td>4.27</td><td>45.12</td>
</tr>
<tr>
    <td>M90</td><td>40.26%</td><td>1</td><td>10</td><td>100</td><td>0.36</td><td>3.86</td><td>39.68</td><td>0.31</td><td>2.65</td><td>27.43</td><td>0.18</td><td>1.82</td><td>18.12</td>
</tr>
<tr>
    <td>M91</td><td>0.99%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.07</td><td>0.85</td><td>0.23</td><td>1.76</td><td>19.94</td><td>1</td><td>9.99</td><td>99.91</td>
</tr>
<tr>
    <td>M92</td><td>9.09%</td><td>1</td><td>10</td><td>100</td><td>0.05</td><td>0.83</td><td>7.46</td><td>0.26</td><td>5.11</td><td>50.45</td><td>0</td><td>0.11</td><td>1.07</td>
</tr>
<tr>
    <td>M93</td><td>9.08%</td><td>1</td><td>10</td><td>100</td><td>0.02</td><td>0.08</td><td>1.15</td><td>0.27</td><td>2.12</td><td>20.97</td><td>0.44</td><td>3.9</td><td>39.7</td>
</tr>
<tr>
    <td>M94</td><td>20.92%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.1</td><td>1.06</td><td>0.25</td><td>2.82</td><td>26.89</td><td>0.31</td><td>3.86</td><td>39.68</td>
</tr>
<tr>
    <td>M95</td><td>7.69%</td><td>1</td><td>10</td><td>100</td><td>0</td><td>0.08</td><td>0.79</td><td>0.25</td><td>2.97</td><td>30.46</td><td>0.07</td><td>0.97</td><td>9.01</td>
</tr>
<tr>
    <td>M96</td><td>33.30%</td><td>1</td><td>10</td><td>100</td><td>0.07</td><td>0.79</td><td>9.39</td><td>0.32</td><td>2.84</td><td>30.8</td><td>0.94</td><td>8.95</td><td>78.89</td>
</tr>
<tr>
    <td>M97</td><td>99%</td><td>1</td><td>10</td><td>100</td><td>1</td><td>10</td><td>99.99</td><td>0.27</td><td>2.32</td><td>25.72</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M98</td><td>97.05%</td><td>1</td><td>10</td><td>100</td><td>0.96</td><td>9.7</td><td>97.09</td><td>0.31</td><td>3.16</td><td>29.87</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M99</td><td>53%</td><td>1</td><td>10</td><td>100</td><td>0.53</td><td>5.3</td><td>53.12</td><td>0.41</td><td>3.96</td><td>39.25</td><td>0.54</td><td>5.89</td><td>54.15</td>
</tr>
<tr>
    <td>M100</td><td>29.35%</td><td>1</td><td>10</td><td>100</td><td>0.3</td><td>2.9</td><td>28.87</td><td>0.28</td><td>2.99</td><td>19.74</td><td>0.27</td><td>4.56</td><td>25.04</td>
</tr>
<tr>
    <td>M101</td><td>50%</td><td>1</td><td>10</td><td>100</td><td>0.5</td><td>5</td><td>49.89</td><td>0.41</td><td>3.4</td><td>33.6</td><td>1</td><td>10</td><td>100</td>
</tr>
<tr>
    <td>M102</td><td>14.35%</td><td>1</td><td>10</td><td>100</td><td>0.14</td><td>1.43</td><td>14.35</td><td>0.24</td><td>2.79</td><td>26.14</td><td>0.34</td><td>8.3</td><td>78.6</td>
</tr>
<tr>
    <td>M103</td><td>26%</td><td>1</td><td>10</td><td>100</td><td>0.14</td><td>1.92</td><td>19.78</td><td>0.22</td><td>2.38</td><td>24.53</td><td>0.44</td><td>7.33</td><td>71.14</td>
</tr>
<tr>
    <td>M104</td><td>4.13%</td><td>1</td><td>10</td><td>100</td><td>0</td><td>0.41</td><td>4</td><td>0.22</td><td>2.38</td><td>24.63</td><td>0.74</td><td>7.74</td><td>69.53</td>
</tr>
<tr>
    <td>M105</td><td>1.58%</td><td>1</td><td>10</td><td>100</td><td>0.01</td><td>0.1</td><td>1.06</td><td>0.02</td><td>0.28</td><td>3</td><td>0.68</td><td>7.13</td><td>69.63</td>
</tr>
<tr>
    <td>M106</td><td>10.00%</td><td>1</td><td>10</td><td>100</td><td>0.07</td><td>0.32</td><td>3.14</td><td>0.02</td><td>0.27</td><td>2.61</td><td>0.43</td><td>6.72</td><td>48</td>
</tr>
<tr>
    <td>M107</td><td>14.35%</td><td>1</td><td>10</td><td>100</td><td>0.14</td><td>1.43</td><td>14.35</td><td>0.16</td><td>1.94</td><td>20.43</td><td>0.58</td><td>6.72</td><td>47.61</td>
</tr>
<tr>
    <td>M108</td><td>18.12%</td><td>1</td><td>10</td><td>100</td><td>0.14</td><td>1.92</td><td>19.78</td><td>0.31</td><td>3.29</td><td>35.21</td><td>0.42</td><td>4.62</td><td>65.43</td>
</tr>
<tr>
    <td>M109</td><td>26%</td><td>1</td><td>10</td><td>100</td><td>0.26</td><td>2.61</td><td>26.21</td><td>0.01</td><td>2.24</td><td>32.72</td><td>0.53</td><td>5.36</td><td>53.66</td>
</tr>
<tr>
    <td>M110</td> <td>0.99%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.01</td> <td>0.07</td> <td>0.85</td> <td>0</td> <td>0.24</td> <td>2.72</td> <td>0.71</td> <td>7.23</td> <td>77.82</td>
</tr>
<tr>
    <td>M111</td> <td>9.09%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.07</td> <td>0.79</td> <td>9.39</td> <td>0.17</td> <td>1.92</td> <td>12.8</td> <td>0.46</td> <td>4.67</td> <td>37.32</td>
</tr>
<tr>
    <td>M112</td> <td>9.08%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.07</td> <td>0.79</td> <td>9.39</td> <td>0.17</td> <td>1.92</td> <td>12.8</td> <td>0.52</td> <td>5.35</td> <td>42.28</td>
</tr>
<tr>
    <td>M113</td> <td>20.92%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.29</td> <td>2.09</td> <td>21</td> <td>0.39</td> <td>3.22</td> <td>24.41</td> <td>0.52</td> <td>5.34</td> <td>53.93</td>
</tr>
<tr>
    <td>M114</td> <td>50%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.5</td> <td>5</td> <td>49.89</td> <td>0.2</td> <td>2.13</td> <td>53.3</td> <td>0.74</td> <td>7.6</td> <td>37.93</td>
</tr>
<tr>
    <td>M115</td> <td>10%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.07</td> <td>0.79</td> <td>9.39</td> <td>0.17</td> <td>1.92</td> <td>12.8</td> <td>0.95</td> <td>9.73</td> <td>42.28</td>
</tr>
<tr>
    <td>M116</td> <td>14.35%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.14</td> <td>1.43</td> <td>14.35</td> <td>0.18</td> <td>2.56</td> <td>17.76</td> <td>0.52</td> <td>5.68</td> <td>46.05</td>
</tr>
<tr>
    <td>M117</td> <td>26%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.02</td> <td>0.26</td> <td>26</td> <td>0.06</td> <td>1.39</td> <td>29.41</td> <td>0.59</td> <td>5.97</td> <td>50.49</td>
</tr>
<tr>
    <td>M118</td> <td>10%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.1</td> <td>1</td> <td>10</td> <td>0.14</td> <td>2.13</td> <td>13.41</td> <td>0.34</td> <td>3.45</td> <td>36.27</td>
</tr>
<tr>
    <td>M119</td> <td>14.35%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.14</td> <td>1.43</td> <td>14.35</td> <td>0.18</td> <td>2.56</td> <td>17.76</td> <td>0.32</td> <td>3.2</td> <td>31.93</td>
</tr>
<tr>
    <td>M120</td> <td>18.12%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.18</td> <td>1.82</td> <td>18.12</td> <td>0.22</td> <td>2.95</td> <td>21.53</td> <td>0.24</td> <td>2.45</td> <td>26.93</td>
</tr>
<tr>
    <td>M121</td> <td>26%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.21</td> <td>2.3</td> <td>22.56</td> <td>0.25</td> <td>3.86</td> <td>25.97</td> <td>0.28</td> <td>2.87</td> <td>28.78</td>
</tr>
<tr>
    <td>M122</td> <td>8.10%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.08</td> <td>0.81</td> <td>8.34</td> <td>0.12</td> <td>2.37</td> <td>11.75</td> <td>0.32</td> <td>3.28</td> <td>37.32</td>
</tr>
<tr>
    <td>M123</td> <td>4.13%</td> <td>1</td> <td>10</td> <td>100</td> <td>0</td> <td>0.41</td> <td>4</td> <td>0.04</td> <td>1.97</td> <td>7.41</td> <td>0.35</td> <td>3.54</td> <td>35.67</td>
</tr>
<tr>
    <td>M124</td> <td>99.08%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.9</td> <td>9</td> <td>99</td> <td>0.94</td> <td>10</td> <td>100</td> <td>0.78</td> <td>7.89</td> <td>78.05</td>
</tr>
<tr>
    <td>M125</td> <td>0.99%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.01</td> <td>0.07</td> <td>0.85</td> <td>0.05</td> <td>1.63</td> <td>4.26</td> <td>0.23</td> <td>2.31</td> <td>28.71</td>
</tr>
<tr>
    <td>M126</td> <td>9.09%</td> <td>1</td> <td>10</td> <td>100</td> <td>0.07</td> <td>0.79</td> <td>9.39</td> <td>0.11</td> <td>2.35</td> <td>12.8</td> <td>0.35</td> <td>3.54</td> <td>35.8</td>
</tr>
<tr>
    <td>M127</td> <td>8.09%</td> <td>1</td> <td>10</td> <td>99</td> <td>0.06</td> <td>0.82</td> <td>7.74</td> <td>0.1</td> <td>2.38</td> <td>11.15</td> <td>0.62</td> <td>6.31</td> <td>62.71</td>
</tr>
<tr>
    <td>M128</td> <td>49.75%</td> <td>1</td> <td>10</td> <td>95</td> <td>0.48</td> <td>5.23</td> <td>50.12</td> <td>0.76</td> <td>5.73</td> <td>55.28</td> <td>0.03</td> <td>1.1</td> <td>10.86</td>
</tr>
<tr>
    <td>M129</td> <td>7.87%</td> <td>1</td> <td>8</td> <td>84</td> <td>0</td> <td>0.08</td> <td>0.78</td> <td>0</td> <td>0.08</td> <td>0.88</td> <td>0.35</td> <td>4.05</td> <td>40.34</td>
</tr>
<tr>
    <td>M130</td> <td>7.87%</td> <td>1</td> <td>8</td> <td>84</td> <td>0.07</td> <td>0.78</td> <td>7.87</td> <td>0.19</td> <td>9.87</td> <td>20.87</td> <td>0.13</td> <td>0.92</td> <td>9.38</td>
</tr>
<tr>
    <td>M131</td> <td>35%</td> <td>1</td> <td>7</td> <td>78</td> <td>0.39</td> <td>3.35</td> <td>34.78</td> <td>0.51</td> <td>3.67</td> <td>47.78</td> <td>0.38</td> <td>4.02</td> <td>40.21</td>
</tr>
<tr>
    <td>M132</td> <td>0.97%</td> <td>1</td> <td>10</td> <td>58</td> <td>0.01</td> <td>0.07</td> <td>1</td> <td>0.13</td> <td>3</td> <td>14</td> <td>0.26</td> <td>5.05</td> <td>17.11</td>
</tr>
<tr>
    <td>M133</td> <td>0.97%</td> <td>1</td> <td>10</td> <td>58</td> <td>0.01</td> <td>0.07</td> <td>1</td> <td>0.41</td> <td>4.12</td> <td>42.17</td> <td>0</td> <td>0</td> <td>0</td>
</tr>
<tr>
    <td>M134</td> <td>49.99%</td> <td>1</td> <td>5</td> <td>53</td> <td>0.6</td> <td>4.94</td> <td>50.24</td> <td>0.56</td> <td>4.96</td> <td>50.86</td> <td>0.96</td> <td>9.76</td> <td>97.08</td>
</tr>
<tr>
    <td>M135</td> <td>0.08%</td> <td>1</td> <td>10</td> <td>37</td> <td>0</td> <td>0.03</td> <td>0.07</td> <td>0</td> <td>0.04</td> <td>1.21</td> <td>0.21</td> <td>2.45</td> <td>20.56</td>
</tr>
<tr>
    <td>M136</td> <td>0.08%</td> <td>1</td> <td>10</td> <td>37</td> <td>0.01</td> <td>0.07</td> <td>0.85</td> <td>0.02</td> <td>0.13</td> <td>0.89</td> <td>0.07</td> <td>0.79</td> <td>9.39</td>
</tr>
<tr>
    <td>M137</td> <td>0.08%</td> <td>1</td> <td>10</td> <td>37</td> <td>0</td> <td>0.08</td> <td>0.79</td> <td>0.13</td> <td>0.88</td> <td>9.16</td> <td>0.26</td> <td>2.34</td> <td>24.69</td>
</tr>
<tr>
    <td>M138</td> <td>3.84%</td> <td>0</td> <td>4</td> <td>53</td> <td>0</td> <td>0.28</td> <td>2.9</td> <td>0.74</td> <td>3.54</td> <td>71.85</td> <td>0.75</td> <td>7.41</td> <td>74.91</td>
</tr>
<tr>
    <td>M139</td> <td>29.08%</td> <td>0</td> <td>4</td> <td>49</td> <td>0.32</td> <td>3.21</td> <td>32.14</td> <td>0.38</td> <td>3.67</td> <td>39.77</td> <td>0.43</td> <td>4.39</td> <td>45.65</td>
</tr>
<tr>
    <td>M140</td> <td>29.08%</td> <td>0</td> <td>4</td> <td>49</td> <td>0.17</td> <td>1.97</td> <td>20.97</td> <td>0.53</td> <td>1.08</td> <td>49.79</td> <td>0.05</td> <td>0.15</td> <td>1.58</td>
</tr>
<tr>
    <td>M141</td> <td>29.08%</td> <td>0</td> <td>4</td> <td>49</td> <td>0.32</td> <td>2.47</td> <td>24.91</td> <td>0.36</td> <td>3.45</td> <td>34.87</td> <td>0.4</td> <td>4.05</td> <td>42</td>
</tr>
<tr>
    <td>M142</td> <td>28.54%</td> <td>0</td> <td>2</td> <td>38</td> <td>0.33</td> <td>3.81</td> <td>38.54</td> <td>0.14</td> <td>2.49</td> <td>98.56</td> <td>1</td> <td>10</td> <td>99.85</td>
</tr>
<tr>
    <td>M143</td> <td>35%</td> <td>0</td> <td>5</td> <td>18</td> <td>0.3</td> <td>3.5</td> <td>35.01</td> <td>0.51</td> <td>4.99</td> <td>49.96</td> <td>0.58</td> <td>4.99</td> <td>50.11</td>
</tr>
<tr>
    <td>M144</td> <td>35%</td> <td>0</td> <td>5</td> <td>18</td> <td>0.39</td> <td>3.35</td> <td>34.78</td> <td>0.74</td> <td>7.32</td> <td>76.89</td> <td>0.07</td> <td>0.76</td> <td>35.01</td>
</tr>
<tr>
    <td>M145</td> <td>35%</td> <td>0</td> <td>5</td> <td>18</td> <td>0.39</td> <td>3.35</td> <td>34.78</td> <td>0.23</td> <td>2.28</td> <td>71.9</td> <td>0.05</td> <td>0.76</td> <td>7.46</td>
</tr>
<tr>
    <td>M146</td> <td>1.58%</td> <td>0</td> <td>5</td> <td>17</td> <td>0.01</td> <td>0.15</td> <td>1.58</td> <td>0.03</td> <td>0.33</td> <td>35.53</td> <td>0.07</td> <td>0.77</td> <td>7.93</td>
</tr>
<tr>
    <td>M147</td> <td>1.58%</td> <td>0</td> <td>5</td> <td>17</td> <td>0.01</td> <td>0.15</td> <td>1.58</td> <td>0.26</td> <td>2.34</td> <td>24.69</td> <td>0.34</td> <td>3.41</td> <td>38.73</td>
</tr>
<tr>
    <td>M148</td> <td>6.45%</td> <td>0</td> <td>1</td> <td>9</td> <td>0.07</td> <td>0.76</td> <td>7.46</td> <td>0.34</td> <td>3.45</td> <td>35.34</td> <td>0.17</td> <td>2.49</td> <td>20.97</td>
</tr>
<tr>
    <td>M149</td> <td>6.45%</td> <td>0</td> <td>1</td> <td>9</td> <td>0.07</td> <td>0.79</td> <td>7.94</td> <td>0.39</td> <td>1.85</td> <td>39.32</td> <td>0.34</td> <td>3.41</td> <td>35.45</td>
</tr>
<tr>
    <td>M150</td> <td>9.09%</td> <td>0</td> <td>0</td> <td>8</td> <td>0.07</td> <td>0.79</td> <td>9.39</td> <td>0.9</td> <td>7.21</td> <td>92.31</td> <td>0.01</td> <td>1.02</td> <td>10.11</td>
</tr>
<tr>
    <td>M151</td> <td>7.69%</td> <td>0</td> <td>0</td> <td>6</td> <td>0.05</td> <td>0.76</td> <td>7.46</td> <td>0.28</td> <td>1.48</td> <td>30.54</td> <td>0.08</td> <td>0.81</td> <td>8.15</td>
</tr>
<tr>
    <td>M152</td> <td>7.94%</td> <td>0</td> <td>0</td> <td>6</td> <td>0.05</td> <td>0.76</td> <td>7.46</td> <td>0.35</td> <td>3.45</td> <td>35.12</td> <td>0.46</td> <td>3.55</td> <td>35.31</td>
</tr>
<tr>
    <td>M153</td> <td>7.94%</td> <td>0</td> <td>0</td> <td>6</td> <td>0.05</td> <td>0.79</td> <td>7.94</td> <td>0.17</td> <td>9.94</td> <td>90.94</td> <td>0</td> <td>0.26</td> <td>2.7</td>
</tr>
<tr>
    <td>M154</td> <td>7.69%</td> <td>0</td> <td>0</td> <td>6</td> <td>0.05</td> <td>0.79</td> <td>7.94</td> <td>0.19</td> <td>2.01</td> <td>20.94</td> <td>0.58</td> <td>5.4</td> <td>50.25</td>
</tr>
<tr>
    <td>M155</td> <td>7.94%</td> <td>0</td> <td>0</td> <td>6</td> <td>0.05</td> <td>0.79</td> <td>7.94</td> <td>0.23</td> <td>2.35</td> <td>23.45</td> <td>0.16</td> <td>2.25</td> <td>20.39</td>
</tr>
<tr>
    <td>M156</td> <td>7.94%</td> <td>0</td> <td>0</td> <td>6</td> <td>0.05</td> <td>0.79</td> <td>7.94</td> <td>0.26</td> <td>2.84</td> <td>28.05</td> <td>0.01</td> <td>0.08</td> <td>1.02</td>
</tr>
<tr>
    <td>M157</td> <td>0.97%</td> <td>0</td> <td>0</td> <td>1</td> <td>0.01</td> <td>0.08</td> <td>1.02</td> <td>0.22</td> <td>2.13</td> <td>4.13</td> <td>0</td> <td>0</td> <td>0</td>
</tr>
<tr>
    <td>M158</td> <td>0.97%</td> <td>0</td> <td>0</td> <td>1</td> <td>0.01</td> <td>0.08</td> <td>1.02</td> <td>0.26</td> <td>2.34</td> <td>24.69</td> <td>0.03</td> <td>0.33</td> <td>35.53</td>
</tr>
<tr>
    <td>M159</td> <td>49.69%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.5</td> <td>4.86</td> <td>49.16</td> <td>0.36</td> <td>5.04</td> <td>49.43</td> <td>0.67</td> <td>8.75</td> <td>74.75</td>
</tr>
<tr>
    <td>M160</td> <td>8.98%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.11</td> <td>1.03</td> <td>9.33</td> <td>0.32</td> <td>3.08</td> <td>12.44</td> <td>0.63</td> <td>6.79</td> <td>37.76</td>
</tr>
<tr>
    <td>M161</td> <td>50.03%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.44</td> <td>4.75</td> <td>50.32</td> <td>0.24</td> <td>6.8</td> <td>53.43</td> <td>0.55</td> <td>5.65</td> <td>58.56</td>
</tr>
<tr>
    <td>M162</td> <td>55.36%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.58</td> <td>5.3</td> <td>55.73</td> <td>0.39</td> <td>3.35</td> <td>58.84</td> <td>0.7</td> <td>7.06</td> <td>84.16</td>
</tr>
<tr>
    <td>M163</td> <td>45.40%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.41</td> <td>4.46</td> <td>45.15</td> <td>0.26</td> <td>6.51</td> <td>48.26</td> <td>0.57</td> <td>5.76</td> <td>57.38</td>
</tr>
<tr>
    <td>M164</td> <td>7.82%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.05</td> <td>0.23</td> <td>2.18</td> <td>0.26</td> <td>2.28</td> <td>5.29</td> <td>0.57</td> <td>5.99</td> <td>59.99</td>
</tr>
<tr>
    <td>M165</td> <td>26.86%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.27</td> <td>2.6</td> <td>26.65</td> <td>0.26</td> <td>4.65</td> <td>29.76</td> <td>0.57</td> <td>8.36</td> <td>55.08</td>
</tr>
<tr>
    <td>M166</td> <td>1.00%</td> <td>0</td> <td>0</td> <td>0</td> <td>0</td> <td>0.09</td> <td>1</td> <td>0.21</td> <td>2.14</td> <td>4.11</td> <td>0.52</td> <td>5.85</td> <td>29.43</td>
</tr>
<tr>
    <td>M167</td> <td>0.35%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.1</td> <td>1.35</td> <td>10.35</td> <td>0.26</td> <td>3.4</td> <td>13.46</td> <td>0.57</td> <td>7.11</td> <td>38.78</td>
</tr>
<tr>
    <td>M168</td> <td>10.35%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.1</td> <td>1</td> <td>10</td> <td>0.31</td> <td>3.05</td> <td>13.11</td> <td>0.11</td> <td>1.12</td> <td>9.64</td>
</tr>
<tr>
    <td>M169</td> <td>10.35%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.1</td> <td>1.03</td> <td>10.35</td> <td>0.31</td> <td>3.08</td> <td>13.46</td> <td>0.32</td> <td>3.19</td> <td>14.56</td>
</tr>
<tr>
    <td>M170</td> <td>45.40%</td> <td>0</td> <td>0</td> <td>0</td> <td>0.41</td> <td>4.46</td> <td>45.15</td> <td>0.23</td> <td>4.12</td> <td>48.26</td> <td>0.24</td> <td>4.23</td> <td>49.36</td>
</tr>
<tr>
        <td>M171</td>
        <td>29.08%</td>
        <td rowspan="8" colspan="3">Non-convergent</td>
        <td>0.34</td> <td>2.97</td> <td>30.31</td> <td>0.19</td> <td>5.02</td> <td>33.42</td> <td>0.2</td> <td>5.13</td> <td>34.52</td>
</tr>
<tr>
    <td>M172</td> 
    <td>30%</td> 
    <td>0.1</td> <td>1</td> <td>10</td> <td>0.27</td> <td>3.05</td> <td>13.11</td> <td>0.28</td> <td>3.16</td> <td>14.21</td>
</tr>
<tr>
    <td>M173</td> 
    <td>0.97%</td> 
    <td>0.01</td> <td>0.08</td> <td>1.02</td> <td>0.22</td> <td>2.13</td> <td>4.13</td> <td>0.23</td> <td>2.24</td> <td>5.23</td>
</tr>
<tr>
    <td>M174</td> 
    <td>40.26%</td> 
    <td>0.36</td> <td>3.86</td> <td>39.68</td> <td>0.26</td> <td>5.91</td> <td>42.79</td> <td>0.27</td> <td>6.02</td> <td>43.89</td>
</tr>
<tr>
    <td>M175</td> 
    <td>97.05%</td> 
    <td>0</td> <td>0.09</td> <td>0.97</td> <td>0.21</td> <td>2.14</td> <td>4.08</td> <td>1</td> <td>10</td> <td>100</td>
</tr>
<tr>
    <td>M176</td> 
    <td>53%</td> 
    <td>0.97</td> <td>9.7</td> <td>97</td> <td>0.16</td> <td>3.85</td> <td>40.84</td> <td>0.51</td> <td>4.93</td> <td>49.76</td>
</tr>
<tr>
    <td>M177</td> 
    <td>10.00%</td> 
    <td>0.1</td> <td>1</td> <td>10</td> <td>0.31</td> <td>3.05</td> <td>13.11</td> <td>0</td> <td>0</td> <td>0</td>
</tr>
<tr>
    <td>M178</td> 
    <td>7.87%</td> 
    <td>0.07</td> <td>0.78</td> <td>7.87</td> <td>0.28</td> <td>2.83</td> <td>30.58</td> <td>0.24</td> <td>2.29</td> <td>19.86</td>
</tr>
<tr>
        <th colspan="2"><b>Precision@k</b></th>
        <th>80.59%</th>
        <th>82.52%</th>
        <th>80.64%</th>
        <th>21.07%</th>
        <th>21.19%</th>
        <th>21.67%</th>
        <th>28.30%</th>
        <th>33.19%</th>
        <th>31.03%</th>
        <th>44.33%</th>
        <th>44.20%</th>
        <th>42.10%</th>
    </tr>
    <tr>
        <th colspan="2"><b>Recall@k</b></th>
        <th>76.97%</th>
        <th>83.70%</th>
        <th>88.76%</th>
        <th>21.07%</th>
        <th>71.12%</th>
        <th>97.52%</th>
        <th>28.30%</th>
        <th>91.94%</th>
        <th>98.79%</th>
        <th>44.33%</th>
        <th>89.98%</th>
        <th>97.07%</th>
    </tr>
  <!-- Add more rows as needed -->
</table>
