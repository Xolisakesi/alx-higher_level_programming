-- Lists all shows in hbtn_0d_tvshows without a linked genre
SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;

