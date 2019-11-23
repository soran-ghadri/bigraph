from _operator import itemgetter

from bigraph.algorithms import jaccard
from helperFunctions.getAdjacents import getAdj2


def jc_predict(G):
    """

    :param G:
    :return:
    """
    start_jc = datetime.now()

    # print('Jaccard prediction starting...')
    dictionary = {}
    out = open('./predictions/jaccard.csv', 'w')
    outN = open('./predictions/jaccard_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    jaccard_sim = defaultdict(dict)
    left_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 0]
    right_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 1]

    out.write('(left_element, right_element)')
    out.write(",")
    out.write('Probability')
    out.write("\n")
    exception_count = 0
    for left_element in left_set:
        hop2s[left_element] = getAdj2(G, list(set(G[left_element])), 1)
        for right_element in right_set:
            neighbors[right_element] = list(set(G[right_element]))
            if not (left_element, right_element) in G.edges:
                try:
                    jaccard_sim[left_element][right_element] = jaccard(hop2s[(left_element)],
                                                                       neighbors[(right_element)])
                    if jaccard_sim[left_element][right_element] > 0:
                        dictionary.update({(left_element, right_element): jaccard_sim[left_element][right_element]})
                except:
                    exception_count += 1
                    print(exception_count)
    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(jaccard_sim[k[0]][k[1]]))
        out.write("\n")