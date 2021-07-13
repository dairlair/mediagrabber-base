from annoy import AnnoyIndex
f = 128
i = AnnoyIndex(f, "euclidean")
i.add_item(0, [-0.1175277978181839, 0.006194942630827427, 0.09368685632944107, -0.10837060958147049, -0.17413435876369476, -0.07749273627996445, -0.06714646518230438, -0.12956055998802185, 0.1784617006778717, -0.1407485157251358, 0.21458278596401215, -0.08269190043210983, -0.1926153004169464, 0.08534427732229233, -0.12016960978507996, 0.12763549387454987, -0.20120210945606232, -0.11935244500637054, -0.010201501660048962, -0.1570747047662735, 0.06396492570638657, 0.017082499340176582, 0.012893480248749256, 0.16222721338272095, -0.0626823902130127, -0.31758859753608704, -0.09845640510320663, -0.008940109051764011, -0.010713169351220131, -0.16833145916461945, 0.05656018853187561, 0.10873913764953613, -0.24918606877326965, 0.01579715870320797, 0.00538557767868042, 0.1254870742559433, -0.04501122608780861, -0.15353628993034363, 0.14307397603988647, 0.051234740763902664, -0.16981978714466095, -0.07532710582017899, 0.12817081809043884, 0.23059788346290588, 0.2262171059846878, 0.004614678211510181, -0.0012476220726966858, -0.1178874522447586, 0.23334378004074097, -0.27405837178230286, 0.07989265769720078, 0.1792898327112198, 0.06635607033967972, 0.019907008856534958, 0.0700962245464325, -0.19381435215473175, 0.0026328759267926216, 0.17253193259239197, -0.1391698569059372, 0.11183469742536545, 0.10855855792760849, -0.10780791193246841, 0.011189926415681839, -0.13548922538757324, 0.1977447122335434, 0.1518968790769577, -0.09468702226877213, -0.19209979474544525, 0.26394566893577576, -0.18745189905166626, -0.0994935855269432, 0.09320057928562164, -0.11826144903898239, -0.19506706297397614, -0.2661926746368408, -0.008235292509198189, 0.47174304723739624, 0.1161770448088646, -0.038836803287267685, 0.08591409027576447, -0.10729658603668213, -0.06681052595376968, -0.07328489422798157, 0.18857745826244354, -0.04124875366687775, 0.023426081985235214, -0.08613626658916473, 0.04816684126853943, 0.23748186230659485, 0.06720481812953949, -0.031201403588056564, 0.26982054114341736, -0.051861703395843506, 0.01342983078211546, 0.04330891743302345, 0.01592675969004631, -0.19535180926322937, 0.013093598186969757, -0.1654219925403595, -0.05895838513970375, -0.1909628063440323, -0.09860527515411377, -0.04885457828640938, 0.08743934333324432, -0.22270134091377258, 0.18898582458496094, -0.06396258622407913, -0.02739563211798668, -0.11697190999984741, -0.04417739436030388, -0.07453422248363495, 0.02770044654607773, 0.13140960037708282, -0.31544363498687744, 0.12936705350875854, 0.11143796145915985, 0.21230703592300415, 0.23015812039375305, 0.0223781056702137, 0.11545857042074203, 0.07630784809589386, -0.10061273723840714, -0.15370361506938934, -0.00728618586435914, -0.04519033432006836, -0.08276654779911041, -0.02678760141134262, 0.08605333417654037])
i.build(10)
r = i.get_nns_by_vector([-0.10527793318033218, 0.08685822784900665, 0.03846986964344978, -0.08109506219625473, 0.017399776726961136, -0.0809638649225235, 0.04280741512775421, -0.14005446434020996, 0.16431693732738495, -0.05231153219938278, 0.21873804926872253, -0.08364284783601761, -0.14817965030670166, -0.1099291518330574, 0.03770197182893753, 0.09919995814561844, -0.09997691214084625, -0.09450426697731018, -0.09624907374382019, -0.16080719232559204, 0.03105194866657257, -0.01797984354197979, 0.042821481823921204, 0.047681525349617004, -0.19584617018699646, -0.2748662829399109, -0.126130148768425, -0.1485724002122879, -0.010682233609259129, -0.0012615022715181112, -0.019983164966106415, 0.047362666577100754, -0.19881868362426758, -0.07327111810445786, -0.0024238070473074913, 0.07991600036621094, 0.02163046970963478, -0.04550030082464218, 0.16111600399017334, 0.1167471706867218, -0.12111915647983551, 0.0452565923333168, -0.004548991098999977, 0.2757042646408081, 0.1900881975889206, 0.019501278176903725, 0.020070569589734077, -0.042307592928409576, 0.14773322641849518, -0.1800721287727356, 0.1159358024597168, 0.08716478943824768, 0.11812607198953629, 0.002430166117846966, 0.12413600087165833, -0.13020996749401093, 0.014906497672200203, 0.06533404439687729, -0.2076835036277771, 0.006672400515526533, 0.03422985598444939, -0.027454039081931114, -0.06762148439884186, -0.04748213663697243, 0.22282370924949646, 0.21972674131393433, -0.12425428628921509, -0.046294204890728, 0.17061085999011993, -0.046621136367321014, 0.01441848836839199, 0.012859499081969261, -0.1577523946762085, -0.12527091801166534, -0.29275304079055786, 0.1567915678024292, 0.4594642221927643, 0.06715807318687439, -0.19537103176116943, 0.0017191991209983826, -0.1362476348876953, 0.0328938364982605, 0.11300597339868546, 0.07165104895830154, -0.09645234793424606, 0.008679554797708988, -0.054123200476169586, 0.02333228290081024, 0.11173051595687866, -0.04031074419617653, -0.0940387099981308, 0.19826391339302063, -0.08137217909097672, 0.05033721402287483, 0.01377633586525917, 0.018525034189224243, -0.13788503408432007, 0.024058038368821144, -0.06175483763217926, -0.000727352686226368, 0.09335647523403168, -0.09035760909318924, -0.003762428183108568, 0.10233903676271439, -0.22115406394004822, 0.06646832078695297, 0.03420666977763176, -0.044367190450429916, -0.02545236423611641, 0.02342313341796398, -0.07415230572223663, -0.033944547176361084, 0.07085979729890823, -0.28462639451026917, 0.158634215593338, 0.13898766040802002, -0.09030432999134064, 0.15479473769664764, 0.06451539695262909, 0.0487838014960289, 0.02501322329044342, 0.030772365629673004, -0.11048459261655807, -0.03730236738920212, 0.06434101611375809, 0.06770958006381989, 0.011986306868493557, 0.04788576811552048], 1)
print ("Annoy: OK")
print (r)
