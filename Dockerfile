FROM golang:alpine AS build-env
WORKDIR /work
ADD ./zip.go /work
RUN go build -o zip zip.go

FROM busybox
COPY --from=build-env /work/zip /usr/local/bin/zip
ENTRYPOINT ["/usr/local/bin/zip"]
