<h1>Pascal Triangle </h1>
<h4>Pascal's triangle contains many patterns. For example, the numerical pattern shown in figure 2 kind of looks like a sock or a stocking, with a long straight portion and then one angled off section at the end. The pattern works in both directions because Pascal's triangle is symmetrical. The sum of any number of terms along one diagonal line in the triangle can be found at the end of that diagonal line just by switching directions. This works as long as you start from a 1 on the edge of the triangle.</h4>

<p>The formula to fill the number in the nth column and mth row of Pascal&#39;s triangle we use the Pascals triangle formula. The formula requires the knowledge of the elements in the (n-1)<sup>th</sup> row, and (m-1)<sup>th</sup> and nth columns. The elements of the n<sup>th</sup> row of Pascal&#39;s triangle are given by, <sup>n</sup>C<sub>0</sub>, <sup>n</sup>C<sub>1</sub>, <sup>n</sup>C<sub>2</sub>, ..., <sup>n</sup>C<sub>n</sub>. The formula for Pascal&#39;s triangle is:</p>

<p><sup>n</sup>C<sub>m</sub> = <sup>n-1</sup>C<sub>m-1 </sub>+ <sup>n-1</sup>C<sub>m</sub></p>

<p>where</p>

<ul>
	<li><sup>n</sup>C<sub>m</sub> represents the (m+1)<sup>th</sup> element in the n<sup>th</sup> row.</li>
	<li>n is a non-negative integer, and</li>
	<li>0 &le; m &le; n.</li>
</ul>

<p>Let us understand this with an example. If we want to find the 3rd element in the 4th row, this means we want to calculate <sup>4</sup>C<sub>2</sub>. Then according to the formula, we get</p>

<p><sup>4</sup>C<sub>2 </sub>= <sup>4-1</sup>C<sub>2-1 </sub>+ <sup>4-1</sup>C<sub>2</sub></p>

<p>&rArr; <sup>4</sup>C<sub>2 </sub>= <sup>3</sup>C<sub>1 </sub>+ <sup>3</sup>C<sub>2</sub></p>

<p>So, this means we need to add the 2nd element in the 3rd row (i.e. 3) with the 3rd element in the 3rd row (i.e. 3.). So our answer will be <sup>4</sup>C<sub>2</sub> = 3 + 3 = 6</p>

<div id="PTBE">
