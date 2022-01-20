--Temp table for yt_data queries
SELECT *
INTO #Temp_Data
FROM (
	SELECT ACSCCOPLIPS.Channel_Id, ACSCCOPLIPS.Channel_Name, ACSCCOPLIPS.Channel_Description, ACSCCOPLIPS.Custom_Url, ACSCCOPLIPS.Channel_Start_Date, 
		ACSCCOPLIPS.Country, ACSCCOPLIPS.Channel_Category, ACSCCOPLIPS.Channel_Banner_Url, ACSCCOPLIPS.Thumbnail_Url,
		ACSCCOPLIPS.Video_Id, V.Video_Duration, ACSCCOPLIPS.Video_Published_At, ACSCCOPLIPS.Date_Published, ACSCCOPLIPS.Video_Title, ACSCCOPLIPS.Video_Description, ACSCCOPLIPS.Playlist_position, 
		ACSCCOPLIPS.Thumbnail_default_url,
		V.tag_1, V.tag_2, V.tag_3, V.tag_4, V.tag_5, V.tag_6, V.tag_7, V.tag_8, V.tag_9, V.tag_10,
		V.tag_11, V.tag_12, V.tag_13, V.tag_14, V.tag_15, V.tag_16, V.tag_17, V.tag_18, V.tag_19, V.tag_20,
		V.tag_21, V.tag_22, V.tag_23, V.tag_24, V.tag_25, V.tag_26, V.tag_27, V.tag_28, V.tag_29, V.tag_30,
		V.View_Count, V.Like_Count, V.Dislike_Count, V.Favorite_Count, V.Comment_Count,
		ACSCCOPLIPS.Comment_0, ACSCCOPLIPS.Likes_0, ACSCCOPLIPS.Date_Published_0, ACSCCOPLIPS.Author_Name_0, ACSCCOPLIPS.Author_YT_Channel_Url_0,
		ACSCCOPLIPS.Comment_1, ACSCCOPLIPS.Likes_1, ACSCCOPLIPS.Date_Published_1, ACSCCOPLIPS.Author_Name_1, ACSCCOPLIPS.Author_YT_Channel_Url_1,
		ACSCCOPLIPS.Comment_2, ACSCCOPLIPS.Likes_2, ACSCCOPLIPS.Date_Published_2, ACSCCOPLIPS.Author_Name_2, ACSCCOPLIPS.Author_YT_Channel_Url_2,
		ACSCCOPLIPS.Comment_3, ACSCCOPLIPS.Likes_3, ACSCCOPLIPS.Date_Published_3, ACSCCOPLIPS.Author_Name_3, ACSCCOPLIPS.Author_YT_Channel_Url_3,
		ACSCCOPLIPS.Activity_Id, ACSCCOPLIPS.Activity_Type,
		ACSCCOPLIPS.Channel_Section_Id, ACSCCOPLIPS.Type_Of_Section, 
		ACSCCOPLIPS.Playlist_Id, ACSCCOPLIPS.Playlist_Title, ACSCCOPLIPS.Playlist_Description, ACSCCOPLIPS.Position_On_Page, ACSCCOPLIPS.Videos_In_Playlist, ACSCCOPLIPS.Playlist_Published_At, 
		ACSCCOPLIPS.Playlist_Url, ACSCCOPLIPS.Playlist_Thumbnail_Default_Url, ACSCCOPLIPS.Embed_Html,
		ACSCCOPLIPS.Related_Video_Id, ACSCCOPLIPS.Related_Video_Published_At, ACSCCOPLIPS.Related_Channel_Id, ACSCCOPLIPS.Related_Channel_Name, ACSCCOPLIPS.Related_Video_Title, ACSCCOPLIPS.Related_Video_Description
	FROM (
		SELECT ACSCCOPLIP.Channel_Id, ACSCCOPLIP.Channel_Name, ACSCCOPLIP.Channel_Description, ACSCCOPLIP.Custom_Url, ACSCCOPLIP.Channel_Start_Date, 
			ACSCCOPLIP.Country, ACSCCOPLIP.Channel_Category, ACSCCOPLIP.Channel_Banner_Url, ACSCCOPLIP.Thumbnail_Url,
			ACSCCOPLIP.Video_Id, ACSCCOPLIP.Video_Published_At, ACSCCOPLIP.Date_Published, ACSCCOPLIP.Video_Title, ACSCCOPLIP.Video_Description, ACSCCOPLIP.Playlist_position, ACSCCOPLIP.Thumbnail_default_url,
			ACSCCOPLIP.Comment_0, ACSCCOPLIP.Likes_0, ACSCCOPLIP.Date_Published_0, ACSCCOPLIP.Author_Name_0, ACSCCOPLIP.Author_YT_Channel_Url_0,
			ACSCCOPLIP.Comment_1, ACSCCOPLIP.Likes_1, ACSCCOPLIP.Date_Published_1, ACSCCOPLIP.Author_Name_1, ACSCCOPLIP.Author_YT_Channel_Url_1,
			ACSCCOPLIP.Comment_2, ACSCCOPLIP.Likes_2, ACSCCOPLIP.Date_Published_2, ACSCCOPLIP.Author_Name_2, ACSCCOPLIP.Author_YT_Channel_Url_2,
			ACSCCOPLIP.Comment_3, ACSCCOPLIP.Likes_3, ACSCCOPLIP.Date_Published_3, ACSCCOPLIP.Author_Name_3, ACSCCOPLIP.Author_YT_Channel_Url_3,
			ACSCCOPLIP.Activity_Id, ACSCCOPLIP.Activity_Type,
			ACSCCOPLIP.Channel_Section_Id, ACSCCOPLIP.Type_Of_Section, 
			ACSCCOPLIP.Playlist_Id, ACSCCOPLIP.Playlist_Title, ACSCCOPLIP.Playlist_Description, ACSCCOPLIP.Position_On_Page, ACSCCOPLIP.Videos_In_Playlist, ACSCCOPLIP.Playlist_Published_At, 
			ACSCCOPLIP.Playlist_Url, ACSCCOPLIP.Playlist_Thumbnail_Default_Url, ACSCCOPLIP.Embed_Html,
			S.Related_Video_Id, S.Related_Video_Published_At, S.Related_Channel_Id, S.Related_Channel_Name, S.Related_Video_Title, S.Related_Video_Description
		FROM (
			SELECT ACSCCOPLI.Channel_Id, ACSCCOPLI.Channel_Name, ACSCCOPLI.Channel_Description, ACSCCOPLI.Custom_Url, ACSCCOPLI.Channel_Start_Date, 
					ACSCCOPLI.Country, ACSCCOPLI.Channel_Category, ACSCCOPLI.Channel_Banner_Url, ACSCCOPLI.Thumbnail_Url,
					ACSCCOPLI.Video_Id, ACSCCOPLI.Video_Published_At, ACSCCOPLI.Date_Published, ACSCCOPLI.Video_Title, ACSCCOPLI.Video_Description, ACSCCOPLI.Playlist_position, ACSCCOPLI.Thumbnail_default_url,
					ACSCCOPLI.Comment_0, ACSCCOPLI.Likes_0, ACSCCOPLI.Date_Published_0, ACSCCOPLI.Author_Name_0, ACSCCOPLI.Author_YT_Channel_Url_0,
					ACSCCOPLI.Comment_1, ACSCCOPLI.Likes_1, ACSCCOPLI.Date_Published_1, ACSCCOPLI.Author_Name_1, ACSCCOPLI.Author_YT_Channel_Url_1,
					ACSCCOPLI.Comment_2, ACSCCOPLI.Likes_2, ACSCCOPLI.Date_Published_2, ACSCCOPLI.Author_Name_2, ACSCCOPLI.Author_YT_Channel_Url_2,
					ACSCCOPLI.Comment_3, ACSCCOPLI.Likes_3, ACSCCOPLI.Date_Published_3, ACSCCOPLI.Author_Name_3, ACSCCOPLI.Author_YT_Channel_Url_3,
					ACSCCOPLI.Activity_Id, ACSCCOPLI.Activity_Type,
					ACSCCOPLI.Channel_Section_Id, ACSCCOPLI.Type_Of_Section, 
					ACSCCOPLI.Playlist_Id, P.Playlist_Title, P.Playlist_Description, ACSCCOPLI.Position_On_Page, P.Videos_In_Playlist, P.Playlist_Published_At, 
					P.Playlist_Url, P.Playlist_Thumbnail_Default_Url, P.Embed_Html 
			FROM (
				SELECT ACSCCO.Channel_Id, ACSCCO.Channel_Name, ACSCCO.Channel_Description, ACSCCO.Custom_Url, ACSCCO.Channel_Start_Date, 
					ACSCCO.Country, ACSCCO.Channel_Category, ACSCCO.Channel_Banner_Url, ACSCCO.Thumbnail_Url,
					ACSCCO.Video_Id, PLI.Video_Published_At, ACSCCO.Date_Published, ACSCCO.Video_Title, ACSCCO.Video_Description, PLI.Playlist_position, ACSCCO.Thumbnail_default_url,
					ACSCCO.Comment_0, ACSCCO.Likes_0, ACSCCO.Date_Published_0, ACSCCO.Author_Name_0, ACSCCO.Author_YT_Channel_Url_0,
					ACSCCO.Comment_1, ACSCCO.Likes_1, ACSCCO.Date_Published_1, ACSCCO.Author_Name_1, ACSCCO.Author_YT_Channel_Url_1,
					ACSCCO.Comment_2, ACSCCO.Likes_2, ACSCCO.Date_Published_2, ACSCCO.Author_Name_2, ACSCCO.Author_YT_Channel_Url_2,
					ACSCCO.Comment_3, ACSCCO.Likes_3, ACSCCO.Date_Published_3, ACSCCO.Author_Name_3, ACSCCO.Author_YT_Channel_Url_3,
					ACSCCO.Activity_Id, ACSCCO.Activity_Type,
					ACSCCO.Channel_Section_Id, ACSCCO.Type_Of_Section, ACSCCO.Playlist_Id, ACSCCO.Position_On_Page
				FROM (
					SELECT ACSC.Channel_Id, ACSC.Channel_Name, ACSC.Channel_Description, ACSC.Custom_Url, ACSC.Channel_Start_Date, ACSC.Country, ACSC.Channel_Category, ACSC.Channel_Banner_Url, ACSC.Thumbnail_Url,
					ACSC.Video_Id, ACSC.Date_Published, ACSC.Video_Title, ACSC.Video_Description, ACSC.Thumbnail_default_url,
					CO.Comment_0, CO.Likes_0, CO.Date_Published_0, CO.Author_Name_0, CO.Author_YT_Channel_Url_0,
					CO.Comment_1, CO.Likes_1, CO.Date_Published_1, CO.Author_Name_1, CO.Author_YT_Channel_Url_1,
					CO.Comment_2, CO.Likes_2, CO.Date_Published_2, CO.Author_Name_2, CO.Author_YT_Channel_Url_2,
					CO.Comment_3, CO.Likes_3, CO.Date_Published_3, CO.Author_Name_3, CO.Author_YT_Channel_Url_3,
					ACSC.Activity_Id, ACSC.Activity_Type,
					ACSC.Channel_Section_Id, ACSC.Type_Of_Section, ACSC.Playlist_Id, ACSC.Position_On_Page
					FROM (
						SELECT ACS.Channel_Id, ACS.Channel_Name, C.Channel_Description, C.Custom_Url, C.Channel_Start_Date, C.Country, C.Channel_Category, C.Channel_Banner_Url, C.Thumbnail_Url,
					ACS.Video_Id, ACS.Date_Published, ACS.Video_Title, ACS.Video_Description, ACS.Thumbnail_default_url, ACS.Activity_Id, ACS.Activity_Type,
					ACS.Channel_Section_Id, ACS.Type_Of_Section, ACS.Playlist_Id, ACS.Position_On_Page
						FROM (
							SELECT A.Channel_Id, A.Channel_Name, A.Video_Id, A.Date_Published, A.Video_Title, A.Video_Description, A.Thumbnail_default_url, A.Activity_Id, A.Activity_Type,
					CS.Channel_Section_Id, CS.Type_Of_Section, CS.Playlist_Id, CS.Position_On_Page
							FROM yt_data..activity AS A
							JOIN yt_data..channel_sections AS CS
							ON A.Channel_Id = CS.Channel_Id
							) as ACS
						JOIN yt_data..channels AS C
						ON ACS.Channel_Id = C.Channel_Id
						) AS ACSC
					JOIN yt_data..comments AS CO
					ON ACSC.Video_Id = CO.Video_Id
					) AS ACSCCO
					left JOIN yt_data..playlist_items AS PLI
					ON ACSCCO.Channel_Id = PLI.Channel_Id AND ACSCCO.Video_Id = PLI.Video_Id AND ACSCCO.Playlist_Id = PLI.Playlist_Id
				) AS ACSCCOPLI
			LEFT JOIN yt_data..playlists AS P
			ON ACSCCOPLI.Playlist_Id = P.Playlist_Id AND ACSCCOPLI.Channel_Id = P.Channel_Id
			) AS ACSCCOPLIP
		LEFT JOIN yt_data..search AS S
		ON ACSCCOPLIP.Video_Id = S.Video_Id
		) AS ACSCCOPLIPS
	LEFT JOIN yt_data..video AS V
	ON ACSCCOPLIPS.Video_Id = V.Video_Id AND ACSCCOPLIPS.Channel_Id = V.Channel_Id
) AS TBL

--1. Channel metadata
SELECT views + redViews AS totalViews, ROUND(likes/dislikes, 0) AS likeRatio, shares AS totalShares, ROUND(videosAddedToPlaylists/(videosAddedToPlaylists + videosRemovedFromPlaylists), 2) AS videosAddedToPlaylistRatio,
	ROUND((estimatedMinutesWatched + estimatedRedMinutesWatched)/60, 2) AS hoursWatched, averageViewPercentage AS avgViewPercentage, subscribersGained - subscribersLost AS subscriberCount
FROM yt_analytics..basic_user_activity_statistics
WHERE video = 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null'

--2. Views by country
SELECT country, views
FROM yt_analytics..user_activity_by_location
WHERE video = 'Null'

--3. Day of Week
SELECT DayOfWeek, SUM(views) AS views, SUM(hoursWatched) AS hoursWatched
FROM (
	SELECT DATENAME(dw, day) AS DayOfWeek, insightPlaybackLocationType, subscribedStatus, SUM(views) AS views, ROUND(SUM(estimatedMinutesWatched)/60, 2) AS hoursWatched
	FROM yt_analytics..video_playback_by_location_by_day
	WHERE subscribedStatus <> 'Null' AND video = 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
	GROUP BY day, insightPlaybackLocationType, subscribedStatus
	) AS Temp
GROUP BY DayOfWeek
ORDER BY views DESC

--4. Weekend vs Weekday
SELECT TypeOfDay,
	CASE
		WHEN TypeOfDay = 'Weekday' THEN ROUND(SUM(views)/5, 2)
		ELSE ROUND(SUM(views)/2, 2)
	END AS avgViews, 
	CASE
		WHEN TypeOfDay = 'Weekday' THEN ROUND(SUM(hoursWatched)/5, 2)
		ELSE ROUND(SUM(hoursWatched)/2, 2)
	END AS avgHoursWatched
FROM (
	SELECT 
		CASE 
			WHEN DayOfWeek IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday') THEN 'Weekday'
			ELSE 'Weekend'
		END AS TypeOfDay, 
		SUM(views) AS views, 
		SUM(hoursWatched) AS hoursWatched
	FROM (
		SELECT DATENAME(dw, day) AS DayOfWeek, insightPlaybackLocationType, subscribedStatus, SUM(views) AS views, ROUND(SUM(estimatedMinutesWatched)/60, 2) AS hoursWatched
		FROM yt_analytics..video_playback_by_location_by_day
		WHERE subscribedStatus <> 'Null' AND video = 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
		GROUP BY day, insightPlaybackLocationType, subscribedStatus
		) AS Temp
	GROUP BY DayOfWeek
	) AS Temp2
GROUP BY TypeOfDay

--5. Audience retention all videos
SELECT elapsedVideoTimeRatio, ROUND(AVG(audienceWatchRatio), 4) AS audienceWatchRatio, ROUND(AVG(relativeRetentionPerformance), 4) AS relativeRetentionPerformance
FROM yt_analytics..audience_retention
WHERE youtubeProduct = 'Null' AND audienceType = 'Null' AND subscribedStatus <> 'Null'
GROUP BY elapsedVideoTimeRatio
ORDER BY elapsedVideoTimeRatio

--6. Traffic source channel
SELECT insightTrafficSourceType, SUM(views) AS views, ROUND(SUM(estimatedMinutesWatched)/60, 2) AS hoursWatched
FROM yt_analytics..traffic_source
WHERE video <> 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY insightTrafficSourceType
ORDER BY views DESC, insightTrafficSourceType

--7. Device and Os channel
SELECT deviceType, operatingSystem, SUM(views) AS views, ROUND(SUM(estimatedMinutesWatched)/60, 2) AS hoursWatched
FROM yt_analytics..operating_system_and_device_type
WHERE video = 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY deviceType, operatingSystem
ORDER BY views DESC

--8. Sub vs unsub metadata
SELECT subscribedStatus, views + redViews AS views, likes, dislikes, shares, ROUND((estimatedMinutesWatched + estimatedRedMinutesWatched)/60, 2) AS hoursWatched, averageViewPercentage
FROM yt_analytics..user_activity_by_location_over_subscribed_status
WHERE (subscribedStatus = 'SUBSCRIBED' OR subscribedStatus = 'UNSUBSCRIBED') AND (video = 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null')

--9. Sub vs unsub metadata by day
SELECT day, subscribedStatus, SUM(views) + SUM(redViews) AS views, SUM(likes) AS likes, SUM(dislikes) AS dislikes, SUM(shares) AS shares,
ROUND(((SUM(estimatedMinutesWatched) + SUM(estimatedRedMinutesWatched))/60), 2) AS hoursWatched, ROUND(AVG(averageViewPercentage), 2) AS averageViewPercentage
FROM yt_analytics..user_activity_by_location_over_subscribed_status_by_day
WHERE subscribedStatus <> 'Null' AND video = 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY day, subscribedStatus
HAVING ROUND(AVG(averageViewPercentage), 2) <= 100
ORDER BY day, subscribedStatus

--10. Sub vs unsub metadata by month
SELECT month, subscribedStatus, SUM(views) + SUM(redViews) AS views, SUM(likes) AS likes, SUM(dislikes) AS dislikes, SUM(shares) AS shares,
ROUND(((SUM(estimatedMinutesWatched) + SUM(estimatedRedMinutesWatched))/60), 2) AS hoursWatched, ROUND(AVG(averageViewPercentage), 2) AS averageViewPercentage
FROM yt_analytics..user_activity_by_location_over_subscribed_status_by_month
WHERE subscribedStatus <> 'Null' AND video = 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY month, subscribedStatus
HAVING ROUND(AVG(averageViewPercentage), 2) <= 100
ORDER BY month, subscribedStatus

--11. Views and subs by day
SELECT day, SUM(views) OVER(ORDER BY day) AS views, SUM(subscribersGained - subscribersLost) OVER(ORDER BY day) as subscribers
FROM yt_analytics..user_activity_by_location_over_time_by_day
WHERE video = 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null'

--12. Views and subs by month
SELECT month, SUM(views) OVER(ORDER BY month) AS views, SUM(subscribersGained - subscribersLost) OVER(ORDER BY month) AS subscribers
FROM yt_analytics..user_activity_by_location_over_time_by_month
WHERE video = 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null'

--13. Audience retention sub vs unsub
SELECT subscribedStatus, elapsedVideoTimeRatio, ROUND(AVG(audienceWatchRatio), 4) AS audienceWatchRatio, ROUND(AVG(relativeRetentionPerformance), 4) AS relativeRetentionPerformance 
FROM yt_analytics..audience_retention
WHERE youtubeProduct = 'Null' AND audienceType = 'Null' AND subscribedStatus <> 'Null'
GROUP BY subscribedStatus, elapsedVideoTimeRatio
ORDER BY elapsedVideoTimeRatio, subscribedStatus

--14. Finding videos sub vs unsub
SELECT insightPlaybackLocationType, subscribedStatus, SUM(views) AS views, ROUND(SUM(estimatedMinutesWatched)/60, 2) AS hoursWatched
FROM yt_analytics..video_playback_by_location
WHERE subscribedStatus <> 'Null' AND video = 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null' AND insightPlaybackLocationType <> 'EMBEDDED'
GROUP BY insightPlaybackLocationType, subscribedStatus
ORDER BY insightPlaybackLocationType

--15. Video metadata
SELECT Meta.Video_Id, Tags.Video_Title, Meta.Length_Of_Video, Meta.Like_Count, Meta.Dislike_Count, Meta.View_Count, Meta.Comment_Count, Tags.Num_Tags, Meta.Time_Published
FROM (
	SELECT Video_Id, 
		CASE
			WHEN LEN(Video_Duration) = 8 THEN CONCAT('00:', SUBSTRING(Video_Duration, PATINDEX('%T%', Video_Duration) + 1, 2), ':', SUBSTRING(Video_Duration, PATINDEX('%M%', Video_Duration) + 1, 2))
			WHEN LEN(Video_Duration) = 7 THEN CASE
												WHEN PATINDEX('%M%', Video_Duration) = 4 
												THEN CONCAT('00:0', SUBSTRING(Video_Duration, PATINDEX('%T%', Video_Duration) + 1, 1), ':', SUBSTRING(Video_Duration, PATINDEX('%M%', Video_Duration) + 1, 2))
												WHEN PATINDEX('%M%', Video_Duration) = 5
												THEN CONCAT('00:', SUBSTRING(Video_Duration, PATINDEX('%T%', Video_Duration) + 1, 2), ':0', SUBSTRING(Video_Duration, PATINDEX('%M%', Video_Duration) + 1, 1))
												END
			WHEN LEN(Video_Duration) = 6 THEN CONCAT('00:0', SUBSTRING(Video_Duration, PATINDEX('%T%', Video_Duration) + 1, 1), ':0', SUBSTRING(Video_Duration, PATINDEX('%M%', Video_Duration) + 1, 1))
			WHEN LEN(Video_Duration) = 5 THEN CASE
												WHEN PATINDEX('%M%', Video_Duration) = 5
												THEN CONCAT('00:', SUBSTRING(Video_Duration, PATINDEX('%T%', Video_Duration) + 1, 2), ':00')
												WHEN PATINDEX('%S%', Video_Duration) = 5
												THEN CONCAT('00:00:', SUBSTRING(Video_Duration, PATINDEX('%T%', Video_Duration) + 1, 2))
												END
			WHEN LEN(Video_Duration) = 4 THEN CASE
												WHEN PATINDEX('%M%', Video_Duration) = 4
												THEN CONCAT('00:0', SUBSTRING(Video_Duration, PATINDEX('%T%', Video_Duration) + 1, 1), ':00')
												WHEN PATINDEX('%S%', Video_Duration) = 4
												THEN CONCAT('00:00:0', SUBSTRING(Video_Duration, PATINDEX('%T%', Video_Duration) + 1, 1))
												END
		END AS Length_Of_Video,
		AVG(CONVERT(INT, Like_Count)) AS Like_Count,
		AVG(CONVERT(INT, Dislike_Count)) AS Dislike_Count,
		AVG(CONVERT(INT, View_Count)) AS View_Count,
		AVG(CONVERT(INT, Comment_Count)) AS Comment_Count,
		SUBSTRING(Date_Published, CHARINDEX('T', Date_Published) + 1, 8) AS Time_Published
	FROM #Temp_Data
	GROUP BY Video_Id, Video_Duration, Like_Count, Dislike_Count, View_Count, Comment_Count, Date_Published
	) AS Meta
JOIN (
	SELECT Video_Id, Video_Title,
		(CASE 
			WHEN tag_1 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_2 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_3 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_4 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_5 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_6 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_7 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_8 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_9 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_10 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_11 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_12 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_13 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_14 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_15 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_16 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_17 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_18 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_19 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_20 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_21 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_22 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_23 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_24 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_25 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_26 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_27 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_28 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_29 <> 'Null' THEN 1
			ELSE 0
		END +
		CASE 
			WHEN tag_30 <> 'Null' THEN 1
			ELSE 0
		END) AS Num_Tags,
		View_Count
	FROM #Temp_Data
	GROUP BY Video_Id, Video_Title, tag_1, tag_2, tag_3, tag_4, tag_5, tag_6, tag_7, tag_8, tag_9, tag_10,
	tag_11, tag_12, tag_13, tag_14, tag_15, tag_16, tag_17, tag_18, tag_19, tag_20,
	tag_21, tag_22, tag_23, tag_24, tag_25, tag_26, tag_27, tag_28, tag_29, tag_30, View_Count
	) AS Tags
ON Meta.Video_Id = Tags.Video_Id
ORDER BY Length_Of_Video DESC

--16. Sub vs unsub by day by vid
SELECT day, subscribedStatus, video, SUM(views) + SUM(redViews) AS views, SUM(likes) AS likes, SUM(dislikes) AS dislikes, SUM(shares) AS shares,
ROUND(((SUM(estimatedMinutesWatched) + SUM(estimatedRedMinutesWatched))/60), 2) AS hoursWatched, ROUND(AVG(averageViewPercentage), 2) AS averageViewPercentage
FROM yt_analytics..user_activity_by_location_over_subscribed_status_by_day
WHERE subscribedStatus <> 'Null' AND video <> 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null' AND averageViewPercentage <= 100
GROUP BY day, subscribedStatus, video
ORDER BY day, subscribedStatus, video

--17. Sub vs unsub by month by vid
SELECT month, subscribedStatus, video, SUM(views) + SUM(redViews) AS views, SUM(likes) AS likes, SUM(dislikes) AS dislikes, SUM(shares) AS shares,
ROUND(((SUM(estimatedMinutesWatched) + SUM(estimatedRedMinutesWatched))/60), 2) AS hoursWatched, ROUND(AVG(averageViewPercentage), 2) AS averageViewPercentage
FROM yt_analytics..user_activity_by_location_over_subscribed_status_by_month
WHERE subscribedStatus <> 'Null' AND video <> 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null' AND averageViewPercentage <= 100
GROUP BY month, subscribedStatus, video
ORDER BY month, subscribedStatus, video

--18. Audience retention each video
SELECT video, elapsedVideoTimeRatio, ROUND(AVG(audienceWatchRatio), 4) AS audienceWatchRatio, ROUND(AVG(relativeRetentionPerformance), 4) AS relativeRetentionPerformance
FROM yt_analytics..audience_retention
WHERE youtubeProduct = 'Null' AND audienceType = 'Null' AND subscribedStatus <> 'Null'
GROUP BY video, elapsedVideoTimeRatio
ORDER BY video, elapsedVideoTimeRatio

--19. Comment polarity data came from table below but numerical code was attained by script in sentiment.py on github.
--21. Funny comments were taken from table below and put into a table and put into tableau no seperate queries.
SELECT Video_Id, Author_Name_0, 
	CASE 
		WHEN Author_Name_0 IS NULL THEN NULL 
		ELSE Comment_0 
	END AS Comment_0, Author_Name_1, 
	CASE 
		WHEN Author_Name_1 IS NULL THEN NULL 
		ELSE Comment_1 
	END AS Comment_1, Author_Name_2, 
	CASE 
		WHEN Author_Name_2 IS NULL THEN NULL 
		ELSE Comment_2 
	END AS Comment_2, Author_Name_3, 
	CASE 
		WHEN Author_Name_3 IS NULL THEN NULL 
		ELSE Comment_3 
	END AS Comment_3
FROM (
	SELECT Video_Id, 
	CASE 
		WHEN Author_Name_0 = 'Concept New Era' THEN NULL 
		ELSE Author_Name_0 
	END AS Author_Name_0, Comment_0, 
	CASE 
		WHEN Author_Name_1 = 'Concept New Era' THEN NULL 
		ELSE Author_Name_1 
	END AS Author_Name_1, Comment_1, 
	CASE 
		WHEN Author_Name_2 = 'Concept New Era' THEN NULL 
		ELSE Author_Name_2 
	END AS Author_Name_2, Comment_2, 
	CASE 
		WHEN Author_Name_3 = 'Concept New Era' THEN NULL 
		ELSE Author_Name_3 
	END AS Author_Name_3, Comment_3
	FROM #Temp_Data
	GROUP BY Video_Id, Author_Name_0, Comment_0, Author_Name_1, Comment_1, Author_Name_2, Comment_2, Author_Name_3, Comment_3
	) AS TEMP
GROUP BY Video_Id, Author_Name_0, Comment_0, Author_Name_1, Comment_1, Author_Name_2, Comment_2, Author_Name_3, Comment_3
ORDER BY Video_Id

--20. Top commentators
SELECT Com_0.Author_Name_0 AS Author_Name, (ISNULL(Num_Comments_0, 0) + ISNULL(Num_Comments_1, 0) + ISNULL(Num_Comments_2, 0) + ISNULL(Num_Comments_3, 0)) AS Tot_Comments
FROM (
	SELECT Author_Name_0, COUNT(DISTINCT COMMENT_0) AS Num_Comments_0
	FROM #Temp_Data
	GROUP BY AUTHOR_NAME_0
	) AS Com_0
FULL OUTER JOIN (
	SELECT Author_Name_1, COUNT(DISTINCT COMMENT_1) AS Num_Comments_1
	FROM #Temp_Data
	GROUP BY AUTHOR_NAME_1
	) AS Com_1
ON Com_0.Author_Name_0 = Com_1.Author_Name_1
FULL OUTER JOIN (
	SELECT Author_Name_2, COUNT(DISTINCT COMMENT_2) AS Num_Comments_2
	FROM #Temp_Data
	GROUP BY AUTHOR_NAME_2
	) AS Com_2
ON Com_0.Author_Name_0 = Com_2.Author_Name_2
FULL OUTER JOIN (
	SELECT Author_Name_3, COUNT(DISTINCT COMMENT_3) AS Num_Comments_3
	FROM #Temp_Data
	GROUP BY AUTHOR_NAME_3
	) AS Com_3
ON Com_0.Author_Name_0 = Com_3.Author_Name_3
Where Author_Name_0 <> 'Concept New Era'
ORDER BY Tot_Comments DESC

--22. Playlist metadata
SELECT ana.playlist, data.Playlist_Title, ana.views + ana.redViews AS views, ana.averageViewDuration, ana.playlistStarts, ana.viewsPerPlaylistStart, data.Videos_In_Playlist
FROM yt_analytics..basic_stats_playlist AS ana
JOIN
yt_data..playlists AS data
ON ana.playlist = data.Playlist_Id
WHERE youtubeProduct = 'Null' AND subscribedStatus = 'Null' AND playlist <> 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
ORDER BY views DESC

--23. Sub vs unsub by playlist
SELECT ana.playlist, data.Playlist_Title, ana.subscribedStatus, SUM(ana.views) AS views, ROUND(SUM(ana.viewsPerPlaylistStart), 2) AS viewsPerPlaylistStart
FROM yt_analytics..traffic_sources_playlist AS ana
JOIN
yt_data..playlists AS data
ON ana.playlist = data.Playlist_Id
WHERE subscribedStatus <> 'Null' AND playlist <> 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY ana.insightTrafficSourceType, ana.playlist, data.Playlist_Title, ana.subscribedStatus
ORDER BY viewsPerPlaylistStart DESC

--24. Sub vs unsub for playlist 
SELECT subscribedStatus, SUM(views) AS views, ROUND(SUM(viewsPerPlaylistStart), 2) AS viewsPerPlaylistStart
FROM yt_analytics..top_playlists
WHERE youtubeProduct = 'CORE' AND subscribedStatus <> 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY subscribedStatus
ORDER BY viewsPerPlaylistStart DESC

--25. Device and Os playlist
SELECT deviceType, operatingSystem, SUM(VIEWS) AS views, ROUND(SUM(viewsPerPlaylistStart), 2) AS viewsPerPlaylistStart
FROM yt_analytics..operating_system_and_device_type_playlist
WHERE youtubeProduct <> 'Null' AND subscribedStatus <> 'Null' AND playlist <> 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY deviceType, operatingSystem
ORDER BY viewsPerPlaylistStart DESC

--26. Finding playlists
SELECT ana.insightTrafficSourceType, ana.playlist, data.Playlist_Title, ana.subscribedStatus, SUM(ana.views) AS views, ROUND(SUM(ana.viewsPerPlaylistStart), 2) AS viewsPerPlaylistStart
FROM yt_analytics..traffic_sources_playlist AS ana
JOIN
yt_data..playlists AS data
ON ana.playlist = data.Playlist_Id
WHERE subscribedStatus <> 'Null' AND playlist <> 'Null' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY ana.insightTrafficSourceType, ana.playlist, data.Playlist_Title, ana.subscribedStatus
ORDER BY viewsPerPlaylistStart DESC

--27. Search Keywords
SELECT insightTrafficSourceDetail, SUM(views) AS views, SUM(estimatedMinutesWatched) AS estimatedMinutesWatched
FROM yt_analytics..traffic_source_details
WHERE insightTrafficSourceType = 'YT_SEARCH' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY insightTrafficSourceDetail
HAVING SUM(views) > 0 AND SUM(estimatedMinutesWatched) > 0
ORDER BY views DESC

--28. Word cloud data is exported from script from sentiment.py on github. Sql below is the data sentiment.py took in to analyze.
SELECT Related_Channel_Name, Related_Video_Title
FROM #Temp_Data
GROUP BY Related_Channel_Name, Related_Video_Title
HAVING Related_Channel_Name <> 'Concept New Era'
ORDER BY Related_Channel_Name

--29. Sharing methods
SELECT sharingService, subscribedStatus, SUM(shares) AS shares
FROM yt_analytics..engagement_and_content_sharing
WHERE subscribedStatus <> 'Null' AND video = 'Null' AND country = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY sharingService, subscribedStatus
ORDER BY shares DESC

--30. Websites to views
SELECT insightTrafficSourceDetail, SUM(views) AS views, SUM(estimatedMinutesWatched) AS estimatedMinutesWatched
FROM yt_analytics..traffic_source_details
WHERE insightTrafficSourceType = 'EXT_URL' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
GROUP BY insightTrafficSourceDetail
HAVING SUM(views) > 0 AND SUM(estimatedMinutesWatched) > 0
ORDER BY views DESC

--31. Top recommended channels from videos
SELECT top 35 Temp.Related_Channel_Name, COUNT(*) AS Times_Related
FROM (
	SELECT Video_Id, Related_Channel_Name
	FROM #Temp_Data
	GROUP BY Video_Id, Related_Channel_Name
	) AS Temp
GROUP BY Temp.Related_Channel_Name
HAVING Temp.Related_Channel_Name <> 'Concept New Era'
ORDER BY Times_Related DESC

--32. Related videos that gave views to cne
SELECT insightTrafficSourceDetail, SUM(views) AS views, SUM(estimatedMinutesWatched) AS estimatedMinutesWatched
FROM yt_analytics..traffic_source_details
WHERE (
	insightTrafficSourceDetail NOT IN (SELECT DISTINCT Video_Id FROM yt_data..video) AND 
	insightTrafficSourceType = 'RELATED_VIDEO' AND country = 'Null' AND province = 'Null' AND continent = 'Null' AND subcontinent = 'Null'
	)
GROUP BY insightTrafficSourceDetail
HAVING SUM(views) > 0 AND SUM(estimatedMinutesWatched) > 0
ORDER BY views DESC, estimatedMinutesWatched DESC