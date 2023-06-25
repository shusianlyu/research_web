import streamlit as st
from ete3 import Tree
from streamlit.components.v1 import html

# Set webpage layout
st.set_page_config(layout="wide")
# Add header
st.header("TA and TE files")
# option files
options = ["TA.fas", "TA.nwk", "TE.fas", "TE.nwk"]

# drop down menu
file = st.selectbox("Select a file", options=options)
js_code = """
<script src="jquery.js"></script>
<script type="text/javascript" src="jquery-svgpan.js"></script>
<script src="treelib.js"></script>
<p><span id="message"></span></p>
<script>

// http://stackoverflow.com/questions/498970/how-do-i-trim-a-string-in-javascript
if (!String.prototype.trim)
{
	String.prototype.trim=function(){return this.replace(/^\s+|\s+$/g, '');};
}

function showtree(element_id)
{
    var t = new Tree();
    var element = document.getElementById(element_id);
    var newick = element.value;
    newick = newick.trim(newick);
	t.Parse(newick);

	if (t.error != 0)
	{
		document.getElementById('message').innerHTML='Error parsing tree';
	}
	else
	{
		document.getElementById('message').innerHTML='Parsed OK';

		t.ComputeWeights(t.root);

		var td = null;

		var selectmenu = document.getElementById('style');
		var drawing_type = (selectmenu.options[selectmenu.selectedIndex].value);

		switch (drawing_type)
		{
			case 'rectanglecladogram':
				td = new RectangleTreeDrawer();
				break;

			case 'phylogram':
				if (t.has_edge_lengths)
				{
					td = new PhylogramTreeDrawer();
				}
				else
				{
					td = new RectangleTreeDrawer();
				}
				break;

			case 'circle':
				td = new CircleTreeDrawer();
				break;

			case 'circlephylogram':
				if (t.has_edge_lengths)
				{
					td = new CirclePhylogramDrawer();
				}
				else
				{
					td = new CircleTreeDrawer();
				}
				break;

			case 'cladogram':
			default:
				td = new TreeDrawer();
				break;
		}

		// clear existing diagram, if any
		var svg = document.getElementById('svg');
		while (svg.hasChildNodes())
		{
			svg.removeChild(svg.lastChild);
		}


		var g = document.createElementNS('http://www.w3.org/2000/svg','g');
		g.setAttribute('id','viewport');
		svg.appendChild(g);


		td.Init(t, {svg_id: 'viewport', width:500, height:500, fontHeight:10, root_length:0.1} );

		td.CalcCoordinates();
		td.Draw();

		// font size
		var cssStyle = document.createElementNS('http://www.w3.org/2000/svg','style');
		cssStyle.setAttribute('type','text/css');

		var font_size = Math.floor(td.settings.height/t.num_leaves);
		font_size = Math.max(font_size, 1);

		var style=document.createTextNode("text{font-size:" + font_size + "px;}");
		cssStyle.appendChild(style);

		svg.appendChild(cssStyle);

		// label leaves...

		var n = new NodeIterator(t.root);
		var q = n.Begin();
		while (q != null)
		{
			if (q.IsLeaf())
			{
				switch (drawing_type)
				{
					case 'circle':
					case 'circlephylogram':
						var align = 'left';
						var angle = q.angle * 180.0/Math.PI;
						if ((q.angle > Math.PI/2.0) && (q.angle < 1.5 * Math.PI))
						{
							align = 'right';
							angle += 180.0;
						}
						drawRotatedText('viewport', q.xy, q.label, angle, align)
						break;

					case 'cladogram':
					case 'rectanglecladogram':
					case 'phylogram':
					default:
						drawText('viewport', q.xy, q.label);
						break;
				}
			}
			q = n.Next();
		}


		// Scale to fit window
		var bbox = svg.getBBox();

		var scale = Math.min(td.settings.width/bbox.width, td.settings.height/bbox.height);


		// move drawing to centre of viewport
		var viewport = document.getElementById('viewport');
		viewport.setAttribute('transform', 'scale(' + scale + ')');

		// centre
		bbox = svg.getBBox();
		if (bbox.x < 0)
		{
			viewport.setAttribute('transform', 'translate(' + -bbox.x + ' ' + -bbox.y + ')');
		}



		// pan
		$('svg').svgPan('viewport');
	}


}

</script>
"""

match file:
    case "TA.fas":
        details = "A file that contains TA (Toxin-Antitoxin) name " \
                  "with actual sequences."
        example = """
        \>Ga0393409_004_36_905
        MASPELEVLGITTVAGNVSVEKTSRNARQICELAGCPQMAVYAGCPRPLLRPLQTAEEVHGKSGIDGANLPEPQMPLGSLHAVQYLIETLMAAQEPVTLALLGPMTNLAVALVQQPRIVERIRRLVFMGGSAFEGNTTPAAEFNIFTDPHAAQIVLSAGIPEVVMLGLNVTQQVLSTPERIERIRALGTRVGQTVADMLAFYGKFDIRRYGLPGGPLHDPCVVAYLLQPQLFELKPCYVEVETASPLNLGRTVVDRWGLSGRPANVQVAFGVDAEEFYRLLTERLGRYR
        """
        st.subheader(details)
        st.write(example)
    case "TA.nwk":
        style_options = ["cladogram", "rectanglecladogram", "phylogram",
                         "circle", "circlephylogram"]
        style = st.selectbox("Select a style", options=style_options)
        details = "A tree represented file of TA's sequences"
        st.subheader(details)
        """tree_file = f"files/column1.nwk"
        t = Tree(tree_file)
        st.write(t)"""
    case "TE.fas":
        details = "A file that contains TE (Transposable Elements) name " \
                  "with actual sequences."
        st.subheader(details)
    case "TE.nwk":
        details = "A tree represented file of TE's sequences"
        st.subheader(details)

