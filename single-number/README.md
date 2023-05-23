<h2>  Single Number</h2><hr><div><p>Given a <strong>non-empty</strong>&nbsp;array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1]
<strong>Output:</strong> 1
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,1,2,1,2]
<strong>Output:</strong> 4
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>
<p> We can use XOR opeartion too , to find out the only unique element  </p>
	
	nums = [2, 4, 3, 2, 4]
	unique = 0

	for num in nums:
   	 unique ^= num

	print(unique)
	
	
Initialize the variable unique to 0.

Iterate through each element num in the nums list.

For each element, perform the XOR operation between the current value of unique and num.

Update the value of unique with the result of the XOR operation.

After iterating through all the elements, the value of unique will hold the unique element from the list.

Now, let's go through the example step by step:

Initialize unique to 0.

Iterate through the nums list.

First iteration: unique ^= 2
unique = 0 ^ 2 = 2
Second iteration: unique ^= 4
unique = 2 ^ 4 = 6
Third iteration: unique ^= 3
unique = 6 ^ 3 = 5
Fourth iteration: unique ^= 2
unique = 5 ^ 2 = 7
Fifth iteration: unique ^= 4
unique = 7 ^ 4 = 3
The final value of unique is 3, which is the unique element in the list [2, 4, 3, 2, 4].

The XOR operation works in such a way that when the same number is XORed twice, it cancels out and returns 0. In this code, all the duplicate elements in the list will be XORed twice, resulting in their elimination from the final result. Only the unique element, which appears once, will remain after the XOR operations.

Therefore, the XOR logic used in the code allows you to find the unique element in a list containing duplicates.
</div>
