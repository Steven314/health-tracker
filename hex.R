library(hexSticker)
library(magick)

sticker(
    "logo.png",
    package = "",
    s_x = 1, s_y = 1,
    s_width = 1,
    h_color = "#860e20",
    white_around_sticker = TRUE,
    filename = "hex.png"
)

p <- image_read("hex.png")
fuzz <- 50
pp <- p %>%
  image_fill(color = "transparent", refcolor = "white", fuzz = fuzz, point = "+1+1") %>%
  image_fill(color = "transparent", refcolor = "white", fuzz = fuzz, point = paste0("+", image_info(p)$width-1, "+1")) %>%
  image_fill(color = "transparent", refcolor = "white", fuzz = fuzz, point = paste0("+1", "+", image_info(p)$height-1)) %>%
  image_fill(color = "transparent", refcolor = "white", fuzz = fuzz, point = paste0("+", image_info(p)$width-1, "+", image_info(p)$height-1))
image_write(image = pp, path = "hex.png")