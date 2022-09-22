# Colour palette generator from a FASTA file
# Alex Pinch
# Referenced Jake Lawlor's PNWColors
# https://github.com/jakelawlor/PNWColors/blob/master/R/PNWColors.R#L2

# 1. Create the color palette from file
dir=readline(prompt="Paste the directory of your FASTA: ")
fasta_palette <- read.csv(file = dir)


# 2. Palette builder function.
palette_builder <- function(name, n, type = c("discrete", "continuous")) {
  pal <- palettes_builder[[name]]
  
  if (is.null(pal)){
    stop("Palette not found.")
  }
  
  if (missing(n)) {
    n <- length(pal[1,])
  }
  
  if (missing(type)) {
    if(n > length(pal[1,])){type <- "continuous"}
    else{ type <- "discrete"}
  }
  type <- match.arg(type)
  
  
  if (type == "discrete" && n > length(pal[1,])) {
    stop("Number of requested colors greater than what discrete palette can offer, \n  use as continuous instead.")
  }
  
  out <- switch(type,
                continuous = grDevices::colorRampPalette(pal[1,])(n),
                discrete = pal[1,][pal[2,] %in% c(1:n)],
  )
  structure(out, class = "palette", name = name)
  
}