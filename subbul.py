import os
filmler = os.listdir(".")

for film in filmler:
	if ".mp4" in film:
		os.system('subliminal download -l tr -e utf8 ' + film)
		orijSub = film.replace('.mp4','.tr.srt')
		esasSub = orijSub.replace('.tr.srt','.srt')
		os.system('mv ' + orijSub + " " + esas
