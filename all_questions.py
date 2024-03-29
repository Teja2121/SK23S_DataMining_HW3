# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "It is true that agglomerative hierarchical clustering is better at handling outliers than k-means because agglomerative checks for the closet pair to match with and if the point is an outlier, then there might not be any other point for it to match with. In k-means the outliers tend to pull the centroid of the cluster in the way of the outlier, effecting the result."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means can have different centroids with the same k-value and it depends on where the centroids are initialized, but it isn't the same case for agglomerative hierarchical clustering."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While take less time and memory than agglomerative hierarchical clustering, it is efficient than agglomerative hierarchical clustering."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "It is false because the new point isn't neccessarily a point present in the cluster and the explanation to SSE is it decreases."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Cohesion is how closely the point are related to each other. So, decrease in SSE means increase in cohesion."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "SSB is distance between two clusters, an increase in SSB means the clusters are far apart which means the seperation is higher."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "They are not independent but dependent because TSS is constant so while k-means is running, the SSE decreases, so SSB should increase, which means that there is a dependency between them."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "SSE+ BSS is TSS which is total sum of squares which is always constant."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Cohesion should be low, which means the points are related to each other and seperation should be high. In K-means, the relation between them is opposite so an increase in cohesion means a decrease in seperation."


    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "It is true that each shaded area has one centroid because as it convergers, the centroid will be at the center of both of the circles."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "As K-means works by minimizing SSE, as some points in the 2nd cluster are closer to the centroid in the first cluster, they may end up in the first centroid's cluster."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The cluster with the centroid 12.5 will be empty because there is no point that is near to it."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    #a = None
    #b = None
    #r = None
    #a_SSE = ((b-r-b)**2+(a-a)**2) + ((b+r-b)**2+(a-a)**2) + ((b-b)**2+(a+r-a)**2) + ((b-b)**2+(a-r-a)**2) #SSE of the 4 data points to centroid
    #a_SSE = (r**2)+(r**2)+(r**2)+(r**2)
    #a_SSE = 4*(r**2)
    answers["(a) SSE"] = "4*(r**2)"

    # type: a string that evaluates to a float
    #b_SSE = ((b-r)**2+(a)**2) + ((b+r)**2+(a)**2) + ((b)**2+(a+r)**2) + ((b)**2+(a-r)**2)
    #b_SSE = (((b)**2 + (r)**2 - (2*b*r) + (a)**2) + ((b)**2 + (r)**2 + (2*b*r) + (a)**2) + ((b)**2 + (a)**2 + (r)**2 + (2*a*r)) + ((b)**2 + (a)**2 + (r)**2 - (2*a*r)))
    #b_SSE = 4 * ((b)**2 + (r)**2 + (a)**2)
    answers["(b) SSE"] = "4 * (a**2 + b**2 + r**2)"

    # type: a string that evaluates to a float
    #for centroid d, distance be a,b on horizontal and vertical axis.
    #the bottom points be the u', v', w', x' be the mirror image of top points, then:
    #total_sse = sse(u) + sse(v) + sse(w) + sse(x) + sse(u') + sse(v') + sse(w') + sse(x')
    #sse(u) = ((a-a)**2) + ((b-(b+(3/2)*r))**2) = ((3/2) * r)**2
    #sse(v) = ((a-(a-(r/2))**2) + ((b-(b+r))**2) = ((r/2)**2) + (r**2)
    #sse(w) = ((a-(a+(r/2)))**2) + ((b-(b+r))**2) = ((r/2)**2) + (r**2)
    #sse(x) = ((a-a)**2) + (y-(y+(r/2)))**2 = (r/2)**2
    #sse(x') = ((a-a)**2) + (y-(y-(r/2)))**2 = (r/2)**2
    #sse(v') = ((a-(a-(r/2))**2) + ((b-(b-r))**2) = ((r/2)**2) + (r**2)
    #sse(w') = ((a-(a+(r/2)))**2) + ((b-(b-r))**2) = ((r/2)**2) + (r**2)
    #sse(u') = ((a-a)**2) + ((b-(b-(3/2)*r))**2) = ((3/2) * r)**2
    #total_sse = ((3/2) * r)**2 + ((r/2)**2) + (r**2) + ((r/2)**2) + (r**2) + (r/2)**2 + (r/2)**2 + ((r/2)**2) + (r**2) + ((r/2)**2) + (r**2) + ((3/2) * r)**2
    #total_sse = 10*(r**2)
    answers["(c) SSE"] = "10*(r**2)"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Here as the algorithm progresses, the left centroid and right centroid gets assingned to circle A and circle C respectively to reduce SSE and also as the circles are nearly at the same distance."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "As the circles are nearly at the same distance, the centroid in circle A remains in A and the right centroid in B gets assigned to circlce C to reduce SSE."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "As the distance between circles B and C is more than the distance between circles A and B, the centroid in A will come out of cirlce A to accomadate the points in circle A and B. The centroids in circles C remain in the circle because the distane would increase if they move out from the circle C."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set(['Group A', 'Group B'])

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The MIN distance between group A and group B is smaller than min distance between group A and group c and also smaller than min distance between group B and group C."

    # type: set
    answers["(b)"] = set(['Group A', 'Group C'])

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Complete linkage works by selecting the minimum of the largest pairwise distance between the clusters, So this means the maximum distance between A and C is less when compared to the maximum distance between group B, group C and also group A, group B."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set(['B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'])

    # type: set
    answers["(a) boundary"] = set(['D', 'G'])

    # type: set
    answers["(a) noise"] = set(['A', 'H'])

    # type: set
    answers["(b) cluster 1"] = set(['A'])

    # type: set
    answers["(b) cluster 2"] = set(['B', 'C', 'D', 'E', 'F', 'G'])

    # type: set
    answers["(b) cluster 3"] = set(['H'])

    # type: set
    answers["(b) cluster 4"] = set(['I', 'J', 'L', 'M'])

    # type: set
    answers["(c)-a core"] = set(['B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'L', 'M'])

    # type: set
    answers["(c)-a boundary"] = set(['A', 'H'])

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    # type: set
    answers["(c)-b cluster 2"] = set(['H', 'I', 'J', 'L', 'M'])

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 had the largest clustering entropy because all the points are nearly even in this cluster and this results in a high entropy."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 seems to have the least entropy because nearly all the points appear to be in water, which results in low entropy."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The diagonal entries seem to be very closely packed, indicating lesser intra cluster distance when comapred to the other matrices and only dataset Z has all entries closely packed."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "As the diagonal entries indicate cluster A,B,C,D from top to bottm, we can see that cluster B and cluster D which is inter cluster distance has the maximum distance, thus indicated by the color red in dataset Z."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Intra cluster distance in B and C appear to be small and they are closely packed hence the dark blue color, while A and D have lesser density hence the lighter shade of dark blue color."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "The distance between A and D (inter cluster distance) appear to be the largeset hence the red coloring and B and C are relatively closer hence the light blue shade."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The clusters B and C has the lowest intra cluster distance hence the darkest blue while A and D have a lesser shade of dark blue because the intra cluster distance is more than B and C"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "The intercluster distance between B and D is the largest so it is colored red."

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The distance between A and D is high so the last column of row 1 should be red which is the case for 1st row of the matrix."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The distance between B and C is small so the 3rd column should be somewhat blue and the fourth column is the distance between B and D which should be more distance so greenish color, which is the 2nd row."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The first column should be greenish because the distance between C and A is high, which is the 3rd row."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The distance between D and A is high, so the first column should be red, which is the 4th row."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical','overlapping','partial']

    # type: list
    answers["(b)"] = ['partitional','exclusive','complete']

    # type: list
    answers["(c)"] = ['partitional','exclusive','complete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping','partial']

    # type: list
    answers["(e)"] = ['partitional','exclusive','complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "It is because every student will get a grade so complete, exclusive because no student can get 2 grades and partitional because students are divided according to their grade."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "Yes"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In both cases DBSCAN might work as the density in the regions might be enough for the DBSCAN algorithm to work in figure a and figure b, provided we choose the min points and radius carefully. DBSCAN might work better in figure (a) when compared to figure (b)"

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "No"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means might not work in both the cases because when clustering, k-means assumes a globular shape and somewaht similar density. This isn't the case in both of the figures."

    # type: string
    answers["(c)"] = "agglomerative hierarchical clustering"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
