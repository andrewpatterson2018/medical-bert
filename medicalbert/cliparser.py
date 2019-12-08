import argparse


def setup_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--train_from_checkpoint",
                        default=None,
                        type=str,
                        help="Continue training from a saved model.")

    parser.add_argument("--train",
                        action='store_true',
                        help="Whether to run training.")

    parser.add_argument("--eval",
                        action='store_true',
                        help="Whether to run eval on the dev set.")
    parser.add_argument("--use_model",
                        default=None,
                        type=str,
                        help="Use this model for evaluations")
    parser.add_argument("--data_dir",
                        default=None,
                        type=str,
                        help="location of input data")
    parser.add_argument("--training_data",
                        default=None,
                        type=str,
                        help="name of training file")
    parser.add_argument("--valid_data",
                        default=None,
                        type=str,
                        help="name of validation file")
    parser.add_argument("--seed",
                        default=None,
                        type=int,
                        help="random seed")
    parser.add_argument("--device",
                        default=None,
                        type=str,
                        help="cpu or cuda")
    parser.add_argument("--experiment_name",
                        default=None,
                        type=str,
                        help="name of the experiment")
    parser.add_argument("--learning_rate",
                        default=None,
                        type=float,
                        help="learning_rate")
    parser.add_argument("--pretrained_model",
                        default=None,
                        type=str,
                        help="pretrained model to train upon.")
    parser.add_argument("--tokenizer",
                        default=None,
                        type=str,
                        help="tokenizer model to use")
    parser.add_argument("--num_train_examples",
                        default=None,
                        type=int,
                        help="number of training examples")
    parser.add_argument("--target",
                        default=None,
                        type=str,
                        help="target column")
    parser.add_argument("--classifier",
                        default=None,
                        type=str,
                        help="classifier to use")
    parser.add_argument("--epochs",
                        default=None,
                        type=int,
                        help="Number of epochs to train for")
    parser.add_argument("--train_batch_size",
                        default=None,
                        type=int,
                        help="batch size during training phase")
    parser.add_argument("--gradient_accumulation_steps",
                        default=None,
                        type=int,
                        help="used to reduce GPU memory footprint")
    parser.add_argument("--datareader",
                        default=None,
                        type=str,
                        help="approach to reading the data from files.")
    return parser.parse_args()
