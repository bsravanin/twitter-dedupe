/**
 * All My Tweets
 * © 2011 Airtight Interactive.
 * www.airtight.cc
 */

var _id, _page_id, _loadedCount, _totalTweets, _ajax;

$(document).ready(function() {

	$("#loader").hide();
	$("#status").hide();
	$("#profile_img").hide();

	$('#target').submit(function() {
		onUserInput($("#input_name").val());
		return false;
	});

	$(window).hashchange(function() {
		onHashChange()
	})
	onHashChange();
});
function onUserInput(id) {
	window.location.hash = id;
}

function onHashChange() {
	//reset
	$("#profile_img").hide();
	$("#tweets ul").empty();
	$("#intro").show();
	$("#loader").hide();
	$("#status").hide();
	$("#user_name").hide();
	if(_ajax)
		_ajax.abort();

	$("#input_name").val("");

	if(window.location.hash) {
		getTweets(window.location.hash.substr(1));
	}

	//track hash tags based on http://stackoverflow.com/questions/4811172/is-it-possible-to-track-hash-links-like-pages-with-google-analytics
	 _gaq.push(['_trackPageview',location.pathname + location.search  + location.hash]);


}

function getTweets(id) {
	_id = id;

	if(_id === "") {
		return;
	}

	$("#intro").hide();
	$("#status").show();
	$("#user_name").show();
	$("#user_name").text(_id);
	$("#status").text("loading tweets");

	//get profile img
	var url = "http://api.twitter.com/1/users/lookup.json?screen_name=" + _id + "&callback=?";

	$.getJSON(url, function(data) {
		$("#profile_img").show();
		$("img#profile_img").attr("src", data[0]["profile_image_url"]);
		_totalTweets = data[0]["statuses_count"];
	});
	_page_id = 1;
	_loadedCount = 0;

	$("#loader").show();

	getPage();

}

function getPage() {

	var url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + _id + "&count=100&page=" + _page_id + "&include_rts=1&trim_user=true&include_entities=false&callback=?";
	_ajax = $.getJSON(url, function(data) {

		$.each(data, function(i, item) {
			console.log(item);
			$("#tweets ul").append("<li>" + item.text.linkify() + " <span class='created_at'>" + format_time(item.created_at) + "</span> <a href='https://twitter.com/#!/" + _id + "/status/" + item.id_str + "'><img src='css/extlink.png'></img></a></li>");
		});
		if(data.length > 0) {
			_loadedCount += data.length;
			_page_id++;
			getPage();

			$("#status").text("loaded " + _loadedCount + " out of " + _totalTweets + " tweets");

		} else {
			//done
			$("#loader").hide();
		}

	});
}

String.prototype.linkify = function() {
	return this.replace(/[A-Za-z]+:\/\/[A-Za-z0-9-_]+\.[A-Za-z0-9-_:%&\?\/.=]+/, function(m) {
		return m.link(m);
	});
};
function format_time(time_value) {
	var values = time_value.split(" ");
	time_value = values[1] + " " + values[2] + ", " + values[5];
	return time_value;
}

function twitter_callback() {
	return true;
}